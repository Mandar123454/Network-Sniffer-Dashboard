# User Guide - Network Sniffer Dashboard

<div align="center">

## 🕵️ Network Sniffer Dashboard User Guide

Complete guide to using the Network Sniffer Dashboard for network packet analysis.

</div>

---

## 📖 Table of Contents

1. [Getting Started](#getting-started)
2. [Dashboard Overview](#dashboard-overview)
3. [Capturing Packets](#capturing-packets)
4. [Filtering & Searching](#filtering--searching)
5. [Analyzing Traffic](#analyzing-traffic)
6. [Exporting Data](#exporting-data)
7. [Tips & Tricks](#tips--tricks)
8. [Troubleshooting](#troubleshooting)

---

## Getting Started

### Before You Start

⚠️ **Admin/Root Privileges Required**
- **Windows**: Run as Administrator
- **macOS/Linux**: Use `sudo`

### Installation

```bash
# 1. Navigate to project directory
cd network-sniffer

# 2. Create virtual environment (Optional but recommended)
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the application
python app.py  # Windows (as Admin)
sudo python3 app.py  # macOS/Linux
```

### First Login

1. Open browser to `http://localhost:5000`
2. Enter default credentials:
   - **Username**: `admin`
   - **Password**: `admin123`
3. Click "Login"

---

## Dashboard Overview

### 🎯 Main Components

```
┌─────────────────────────────────────────────────────────────┐
│ 🕵️  Network Sniffer Dashboard        [User] [Export] [Logout]│
├─────────────────────────────────────────────────────────────┤
│ ┌─────────────┐ ┌──────────────┐ ┌──────────────┐         │
│ │   Packets   │ │Protocol Stats│ │Category Stats│         │
│ │   Captured  │ │   {TCP:120}  │ │  {DNS: 45}   │         │
│ │    2,450    │ │   {UDP: 80}  │ │ {HTTP: 200}  │         │
│ │  ● Live     │ │   {ICMP: 10} │ │{HTTPS: 150}  │         │
│ └─────────────┘ └──────────────┘ └──────────────┘         │
├─────────────────────────────────────────────────────────────┤
│ [Protocol▼] [Category▼] [Apply] [Search...] [Rows:25▼]     │
├─────────────────────────────────────────────────────────────┤
│ ┌─────────────────────────┐ ┌─────────────────────────┐    │
│ │  Protocol Distribution  │ │  Packet Size Trend      │    │
│ │  [Bar Chart]            │ │  [Line Chart]           │    │
│ └─────────────────────────┘ └─────────────────────────┘    │
├─────────────────────────────────────────────────────────────┤
│ 🔍 Recent Packets                                            │
│ ┌───────────────────────────────────────────────────────┐  │
│ │ Time │ Src IP │ Dst IP │ Proto │ Category │ Len │Info│  │
│ │ 10:23│192.168│8.8.8.8 │ UDP   │   DNS    │ 53  │... │  │
│ │ 10:22│192.168│172.217 │ TCP   │  HTTPS   │1460 │... │  │
│ └───────────────────────────────────────────────────────┘  │
│ [Prev] Page 1 / 12 [Next]                                   │
└─────────────────────────────────────────────────────────────┘
```

### 📊 Stats Cards

**Total Packets Captured**
- Shows total count of all packets since start
- Green pulsing dot indicates active sniffing
- Updates in real-time every 2 seconds

**Protocol Stats**
- JSON display of protocol distribution
- Shows count for each protocol type
- Updates dynamically as packets arrive

**Category Stats**
- Shows traffic categorization
- Categories: HTTP, HTTPS, DNS, OTHER
- Helps identify traffic types quickly

---

## Capturing Packets

### How Capture Works

1. **Background Thread**: Packet capture runs in background
2. **Real-time Processing**: Each packet is processed immediately
3. **Memory Storage**: Packets stored in RAM (up to 2,000)
4. **Auto-trim**: Oldest packets removed when limit reached

### What Gets Captured

✅ **Captured**
- All network traffic from your interfaces
- Packets going in and out
- All protocols (TCP, UDP, ICMP, etc.)

❌ **Not Captured**
- Encrypted payload content
- Traffic from other machines (typically)
- Local system calls

### Starting/Stopping

**Start**: Run `python app.py`
```
Output:
 * Running on http://0.0.0.0:5000
 * Press CTRL+C to quit
```

**Stop**: Press `CTRL+C` in terminal

---

## Filtering & Searching

### Protocol Filter

**Filter by specific protocols:**

| Protocol | Description | Common Ports |
|----------|-------------|--------------|
| TCP | Reliable transmission | 80, 443, 22, 3306 |
| UDP | Fast unreliable | 53 (DNS), 67 (DHCP) |
| ICMP | Ping/Echo | N/A |
| ALL | Show everything | All |

**Example:**
```
1. Select Protocol Filter: "TCP"
2. Click "Apply Filters"
3. Only TCP packets shown
```

### Category Filter

**Filter by traffic type:**

| Category | What It Means | Common Uses |
|----------|--------------|------------|
| HTTP | Web traffic (unencrypted) | Web browsing |
| HTTPS | Secure web traffic | Secure browsing |
| DNS | Domain name lookups | DNS queries |
| OTHER | Everything else | VPN, custom protocols |
| ALL | Show everything | All traffic |

**Example:**
```
1. Select Category Filter: "DNS"
2. Click "Apply Filters"
3. Only DNS lookups shown
4. See what domains your system queries
```

### Search Function

**Find specific packets by:**

- **IP Address**: `192.168.1.1` or `8.8.8.8`
- **Protocol**: `TCP`, `UDP`, `ICMP`
- **Category**: `HTTP`, `DNS`, `HTTPS`
- **Info**: Any text in packet summary

**Examples:**

```
Search: "google.com"
Results: All packets related to Google

Search: "192.168"
Results: All packets to/from 192.168.x.x

Search: "DNS"
Results: All DNS-related packets
```

**Tips:**
- Case-insensitive
- Partial matches work
- Search updates in real-time
- Multiple criteria: Filter first, then search

### Rows Per Page

**Control pagination:**

| Option | Best For |
|--------|----------|
| 10 | Detailed inspection |
| 25 | Balanced view (default) |
| 50 | Overview of many packets |

---

## Analyzing Traffic

### Understanding Charts

#### Protocol Distribution (Bar Chart)
```
What it shows: How many packets per protocol
When to use: Identify dominant protocols
Example:
  TCP  ▂▄▆█ 1,200 packets
  UDP  ▂▄ 400 packets
  ICMP ▂ 100 packets
```

#### Packet Size Trend (Line Chart)
```
What it shows: Packet sizes over time
When to use: Spot large transfers
Example:
  Large spikes = File transfers
  Consistent = Streaming
  Tiny = DNS/ACK packets
```

### Reading the Packet Table

| Column | What It Shows | Example |
|--------|--------------|---------|
| Time | When captured | 14:35:28 |
| Src IP | Source address | 192.168.1.100 |
| Dst IP | Destination | 8.8.8.8 |
| Proto | Protocol type | TCP, UDP, ICMP |
| Category | Traffic type | HTTP, DNS, HTTPS |
| Len | Packet size in bytes | 1460 |
| Summary | Packet details | TCP 192.168.1.100:54321 > 8.8.8.8:443 S |

### Interpreting Packet Info

```
TCP 192.168.1.100:54321 > 8.8.8.8:443 S
├── Protocol: TCP
├── Source: 192.168.1.100 port 54321
├── Destination: 8.8.8.8 port 443
└── Flag: S (SYN - connection start)

UDP 192.168.1.100:53 > 8.8.8.8:53 
├── Protocol: UDP
├── Source: port 53 (DNS)
└── Destination: port 53 (DNS)
```

### Common Patterns

**DNS Lookup:**
```
Port 53 involved
Category: DNS
Small packet size (< 100 bytes)
```

**Web Browsing:**
```
Port 80 (HTTP) or 443 (HTTPS)
Category: HTTP or HTTPS
Variable packet sizes
```

**Video Streaming:**
```
Protocol: TCP or UDP
Large packets (> 1000 bytes)
Consistent pattern
```

---

## Exporting Data

### PCAP Export

**For professional analysis with Wireshark:**

1. Click **⬇ Export .pcap**
2. File downloads: `network_capture.pcap`
3. Open in Wireshark for detailed analysis

**Use Wireshark to:**
- Examine payload content
- Analyze packet flow
- Perform deep packet inspection
- Create network graphs

**Steps to open in Wireshark:**
```
1. Open Wireshark
2. File → Open
3. Select downloaded .pcap file
4. Analyze in detail
```

### CSV Export

**For spreadsheet analysis:**

1. Click **⬇ CSV** (if available)
2. File downloads: `packets_export.csv`
3. Open in Excel, Google Sheets, etc.

**CSV Contains:**
- Time, Source IP, Destination IP
- Protocol, Category, Packet Length
- Packet Summary

**Analysis Ideas:**
```
Excel/Sheets:
- Create pivot tables by protocol
- Chart IP distributions
- Timeline analysis
- Filter by criteria
```

---

## Tips & Tricks

### 🚀 Performance

- **Limit History**: Start with smaller MAX_HISTORY if slow
- **Filter Early**: Reduce data before searching
- **Clear Browser Cache**: Improves responsiveness
- **Close Other Tabs**: Frees up resources

### 🔍 Advanced Searching

```
Find all Google Traffic:
Search: "172.217" (Google's IP range)

Find all DNS:
Search: "53" (DNS port)
or Filter Category: DNS

Find VPN Traffic:
Search for OpenVPN/WireGuard ports

Find Local Traffic:
Search: "192.168" or "10.0" or "172.16"
```

### 📊 Analysis Techniques

**Identify Suspicious Activity:**
1. Look for unusual ports
2. Check for excessive connections
3. Monitor data transfers
4. Track DNS lookups

**Monitor Specific Services:**
1. Filter by protocol
2. Filter by port number
3. Search for IP ranges
4. Watch real-time flow

**Compare Traffic Patterns:**
1. Export to CSV
2. Analyze in spreadsheet
3. Create charts
4. Compare over time

### ⚡ Keyboard Shortcuts

```
F5 / Ctrl+R        Refresh dashboard
Ctrl+F             Browser find (search table)
Tab                Navigate between filters
Enter              Apply filters
Esc                Close any modals
```

---

## Troubleshooting

### ❌ No Packets Captured

**Causes & Solutions:**

| Problem | Solution |
|---------|----------|
| No admin rights | Run as Administrator (Windows) or use sudo (Mac/Linux) |
| Network idle | Generate traffic by browsing web |
| Interface down | Check network connection |
| Firewall blocking | Check firewall settings |
| VPN active | May require additional setup |

**Test:**
```bash
# Windows: Try pinging
ping 8.8.8.8

# macOS/Linux: Try pinging
ping google.com
```

### ❌ App Won't Start

**Error: Permission Denied**
```bash
# Solution: Use admin rights
# Windows: Run Command Prompt as Admin
# macOS/Linux: Add sudo
sudo python3 app.py
```

**Error: Port 5000 in Use**
```bash
# Find what's using port 5000
# Windows:
netstat -ano | findstr :5000

# macOS/Linux:
lsof -i :5000

# Kill the process (get PID from above)
# Windows: taskkill /PID <PID> /F
# macOS/Linux: kill -9 <PID>

# Or change port in app.py
app.run(host="0.0.0.0", port=5001)
```

### ❌ Low Performance

**Solutions:**
1. Reduce MAX_HISTORY in app.py
2. Clear browser cache
3. Use filtering instead of search
4. Close other applications
5. Restart the app

### ❌ Can't Login

**Issue: Wrong Password**
- Check default: admin / admin123
- Verify CAPS LOCK off
- Reset by editing app.py

**Issue: Session Expired**
- Logout and login again
- Clear cookies
- Restart browser

### ❌ Missing Packets

**Reasons:**
- Memory limit reached (MAX_HISTORY)
- System running low on RAM
- Heavy network traffic
- Slow processing

**Solutions:**
- Export frequently
- Reduce MAX_HISTORY
- Run on more powerful machine

---

## 📞 Getting Help

### Consult Documentation
- README.md - Main documentation
- CONTRIBUTING.md - How to contribute
- CODE_OF_CONDUCT.md - Community guidelines

### Report Issues
- GitHub Issues for bugs
- GitHub Discussions for questions

### Common Questions

**Q: Can I see HTTPS content?**
A: No, encryption prevents payload viewing.

**Q: Does this affect network speed?**
A: Minimal impact, runs in background.

**Q: Can I monitor other computers?**
A: Typically no (requires same network/MITM setup).

**Q: Is this legal to use?**
A: Only on networks you own/authorize.

---

## 🎓 Learning Resources

### Network Fundamentals
- TCP/IP basics
- OSI model layers
- Protocol operation

### Tools to Learn
- Wireshark tutorial
- tcpdump/netsh commands
- Network analysis techniques

### Practice Ideas
1. Monitor your browser traffic
2. Identify service ports
3. Analyze DNS queries
4. Track bandwidth usage

---

<div align="center">

**Happy packet sniffing! 🕵️**

Made with ❤️ by Mandar Kajbaje

</div>
