from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect,
    url_for,
    session,
    send_file,
)
from scapy.all import sniff, IP, TCP, UDP, ICMP, wrpcap
from datetime import datetime
from threading import Thread, Lock
import os
import csv
import io
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "change_this_to_a_random_secret")
app.config['SESSION_COOKIE_SECURE'] = os.getenv('SESSION_COOKIE_SECURE', 'True') == 'True'
app.config['SESSION_COOKIE_HTTPONLY'] = os.getenv('SESSION_COOKIE_HTTPONLY', 'True') == 'True'

# Simple hard-coded auth (for demo / project)
VALID_USERNAME = os.getenv("USERNAME", "admin")
VALID_PASSWORD = os.getenv("PASSWORD", "admin123")

PACKETS_META = []  # dicts for UI
PACKETS_RAW = []   # original scapy packets for pcap export
lock = Lock()
MAX_HISTORY = int(os.getenv("MAX_HISTORY", 2000))


def categorize_packet(pkt):
    """Return high-level category based on ports: HTTP/HTTPS/DNS/OTHER."""
    try:
        sport = None
        dport = None
        if TCP in pkt:
            sport = pkt[TCP].sport
            dport = pkt[TCP].dport
        elif UDP in pkt:
            sport = pkt[UDP].sport
            dport = pkt[UDP].dport

        ports = {sport, dport}
        if 53 in ports:
            return "DNS"
        if 80 in ports or 8080 in ports:
            return "HTTP"
        if 443 in ports:
            return "HTTPS"
    except Exception:
        pass
    return "OTHER"


def capture():
    """Background thread: capture packets using scapy and store in memory."""
    def process(pkt):
        try:
            record = {
                "time": datetime.now().strftime("%H:%M:%S"),
                "src": pkt[IP].src if IP in pkt else None,
                "dst": pkt[IP].dst if IP in pkt else None,
                "len": len(pkt),
                "info": pkt.summary(),
            }

            if TCP in pkt:
                proto = "TCP"
            elif UDP in pkt:
                proto = "UDP"
            elif ICMP in pkt:
                proto = "ICMP"
            elif IP in pkt:
                proto = str(pkt[IP].proto)
            else:
                proto = pkt.name

            record["proto"] = proto
            record["category"] = categorize_packet(pkt)

            with lock:
                PACKETS_META.append(record)
                PACKETS_RAW.append(pkt)

                # trim history
                if len(PACKETS_META) > MAX_HISTORY:
                    del PACKETS_META[:300]
                    del PACKETS_RAW[:300]
        except Exception:
            # ignore malformed/unexpected packets
            pass

    try:
        sniff(prn=process, store=False)  # capture forever
    except PermissionError:
        print("ERROR: Packet capture requires administrator/root privileges.")
        print("Please run this application as Administrator (Windows) or with sudo (Linux).")
        return
    except Exception as e:
        print(f"ERROR: Packet capture failed: {e}")
        print("This may be due to missing network permissions or running in a restricted environment (e.g., Azure App Service).")
        return


# -------------------- Auth Helpers --------------------
def login_required(view_func):
    def wrapper(*args, **kwargs):
        if not session.get("logged_in"):
            return redirect(url_for("login"))
        return view_func(*args, **kwargs)
    wrapper.__name__ = view_func.__name__
    return wrapper


# -------------------- Routes --------------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form.get("username", "")
        pw = request.form.get("password", "")
        if user == VALID_USERNAME and pw == VALID_PASSWORD:
            session["logged_in"] = True
            session["username"] = user
            return redirect(url_for("index"))
        else:
            return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/")
@login_required
def index():
    return render_template("index.html", username=session.get("username", "admin"))


@app.route("/data")
@login_required
def get_data():
    protocol_filter = request.args.get("protocol", "ALL")
    category_filter = request.args.get("category", "ALL")
    limit = int(request.args.get("limit", 200))

    with lock:
        packets = list(PACKETS_META)

    # Filter
    filtered = []
    for p in packets:
        if protocol_filter != "ALL" and p["proto"] != protocol_filter:
            continue
        if category_filter != "ALL" and p["category"] != category_filter:
            continue
        filtered.append(p)

    # Limit
    filtered = filtered[-limit:]

    # Protocol stats
    proto_stats = {}
    cat_stats = {}
    for p in filtered:
        proto_stats[p["proto"]] = proto_stats.get(p["proto"], 0) + 1
        cat_stats[p["category"]] = cat_stats.get(p["category"], 0) + 1

    # For line chart: just use index as x-axis
    size_series = [pkt["len"] for pkt in filtered]
    time_labels = [pkt["time"] for pkt in filtered]

    return jsonify(
        {
            "packets": filtered,
            "stats": proto_stats,
            "cat_stats": cat_stats,
            "total": len(packets),
            "sizes": size_series,
            "time_labels": time_labels,
        }
    )


@app.route("/export_pcap")
@login_required
def export_pcap():
    with lock:
        if not PACKETS_RAW:
            return "No packets to export yet.", 400

        filename = "capture_export.pcap"
        filepath = os.path.join(os.path.dirname(__file__), filename)
        wrpcap(filepath, PACKETS_RAW)

    return send_file(
        filepath,
        as_attachment=True,
        download_name="network_capture.pcap",
    )


@app.route("/export_csv")
@login_required
def export_csv():
    protocol_filter = request.args.get("protocol", "ALL")
    category_filter = request.args.get("category", "ALL")

    with lock:
        packets = list(PACKETS_META)

    # Filter packets
    filtered = []
    for p in packets:
        if protocol_filter != "ALL" and p["proto"] != protocol_filter:
            continue
        if category_filter != "ALL" and p["category"] != category_filter:
            continue
        filtered.append(p)

    if not filtered:
        return "No packets to export.", 400

    # Create CSV in memory
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=["time", "src", "dst", "proto", "category", "len", "info"])
    writer.writeheader()
    writer.writerows(filtered)

    # Convert to bytes
    output.seek(0)
    csv_data = output.getvalue()

    return (
        csv_data,
        200,
        {
            "Content-Type": "text/csv",
            "Content-Disposition": 'attachment; filename="network_packets.csv"',
        },
    )


if __name__ == "__main__":
    # Get port from environment or use default
    port = int(os.getenv("WEBSITES_PORT", 5000))
    debug = os.getenv("FLASK_ENV", "development") == "development"
    
    t = Thread(target=capture, daemon=True)
    t.start()
    
    app.run(host="0.0.0.0", port=port, debug=debug)