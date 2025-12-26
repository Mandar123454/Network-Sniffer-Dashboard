# 🕵️ Network Sniffer Dashboard

<div align="center">

![Network Sniffer](https://img.shields.io/badge/Network-Sniffer-blue?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.7+-green?style=flat-square)
![Flask](https://img.shields.io/badge/Flask-2.0+-red?style=flat-square)
![Scapy](https://img.shields.io/badge/Scapy-Network-orange?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

A powerful, real-time network packet sniffer with a sleek neon-styled web dashboard. Capture, analyze, and export network traffic with ease.

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [Contributing](#contributing) • [License](#license)

</div>

---

## ✨ Features

### 🚀 Core Functionality
- **Real-time Packet Capture**: Monitor network traffic live using Scapy
- **Protocol Detection**: Automatic detection of TCP, UDP, ICMP, and more
- **Traffic Categorization**: Smart categorization (HTTP, HTTPS, DNS, OTHER)
- **Advanced Filtering**: Filter by protocol and traffic category
- **Search & Sort**: Search packets by IP, protocol, or info fields
- **Pagination**: Browse through captured packets efficiently

### 📊 Analytics & Visualization
- **Live Statistics**: Real-time protocol and category distribution
- **Protocol Chart**: Bar chart visualization of protocol distribution
- **Packet Size Trend**: Line chart showing packet size patterns over time
- **Detailed Packet Table**: Complete packet information with sortable columns

### 💾 Export Options
- **PCAP Export**: Export captured packets in industry-standard PCAP format
- **CSV Export**: Export packet metadata to CSV for analysis

### 🔐 Security
- **Session-based Authentication**: Secure login with session management
- **Password Protection**: Demo credentials with production-ready structure
- **HTTPS Ready**: Prepared for SSL/TLS deployment

### 🎨 User Experience
- **Neon Cyberpunk UI**: Modern, dark-themed interface with glowing accents
- **Animated Badge**: Blinking cyber spy hacker logo in header
- **Responsive Design**: Works on desktop and tablet devices
- **Real-time Updates**: Auto-refresh every 2 seconds
- **Dark Mode**: Easy on the eyes during extended use

---

## 📋 Requirements

### System Requirements
- Python 3.7 or higher
- Administrator/Root privileges (required for packet sniffing)
- Windows, macOS, or Linux

### Python Dependencies
- Flask 2.0+
- Scapy 2.4+
- Other standard libraries (datetime, threading, os, json)

---

## 🛠️ Installation

### Step 1: Clone or Download
```bash
git clone https://github.com/yourusername/network-sniffer.git
cd network-sniffer
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install flask scapy
```

### Step 4: Run the Application
```bash
# Windows (requires admin)
python app.py

# macOS/Linux (requires sudo)
sudo python3 app.py
```

### Step 5: Access the Dashboard
Open your browser and navigate to:
```
http://localhost:5000
```

**Default Credentials:**
- Username: `admin`
- Password: `admin123`

---

## 🚀 Usage

### Starting the Sniffer
1. Ensure you have **administrator/root privileges**
2. Run `python app.py` (Windows) or `sudo python3 app.py` (macOS/Linux)
3. Open browser to `http://localhost:5000`
4. Login with default credentials
5. Packets will start capturing in real-time

### Features Guide

#### 📊 Dashboard
- **Total Packets**: Shows count of all captured packets
- **Protocol Stats**: JSON display of protocol distribution
- **Category Stats**: JSON display of traffic categories
- **Live Indicator**: Green pulsing dot shows active sniffing

#### 🔍 Filtering
```
Protocol Filter: TCP, UDP, ICMP, or All
Category Filter: HTTP, HTTPS, DNS, or Other
Apply Filters: Click to apply both filters
Search Box: Search by IP, protocol, category, or info
Rows Per Page: Display 10, 25, or 50 packets
```

#### 📤 Export
- **PCAP Export**: Download raw packet data for Wireshark analysis
- **CSV Export**: Download packet metadata for spreadsheet analysis

#### 📑 Pagination
- Navigate between pages of captured packets
- Shows current page, total pages, and packet count

---

## 📁 Project Structure

```
network-sniffer/
├── app.py                    # Flask application & packet capture logic
├── templates/
│   ├── index.html           # Dashboard page
│   └── login.html           # Login page
├── static/
│   ├── style.css            # Neon styling
│   └── script.js            # Dashboard interactivity
├── README.md                # This file
├── LICENSE                  # MIT License
├── CONTRIBUTING.md          # Contribution guidelines
├── CODE_OF_CONDUCT.md       # Code of conduct
└── requirements.txt         # Python dependencies
```

---

## ⚙️ Configuration

### Edit Default Credentials
Edit `app.py` to change default credentials:
```python
VALID_USERNAME = "admin"
VALID_PASSWORD = "admin123"
```

### Change Server Port
Edit `app.py` to change the port:
```python
app.run(host="0.0.0.0", port=5000, debug=True)
```

### Adjust History Limit
Edit `app.py` to change max stored packets:
```python
MAX_HISTORY = 2000  # Change this value
```

---

## 🔍 How It Works

### Packet Capture Process
1. Flask app starts background thread with `capture()`
2. Scapy `sniff()` continuously captures network packets
3. Each packet is processed and stored in memory
4. Packets are formatted with metadata (time, IP, protocol, size)
5. Oldest packets are trimmed when limit is reached

### Data Flow
```
Packet Capture → Processing → In-Memory Storage → API Endpoint → Dashboard
```

### Protocol Detection
```python
TCP/UDP → Extract ports
↓
Port 53 → DNS
Port 80/8080 → HTTP
Port 443 → HTTPS
Otherwise → OTHER
```

---

## 🚨 Important Notes

### Admin/Root Required
Packet sniffing requires elevated privileges:
- **Windows**: Run Command Prompt as Administrator
- **macOS/Linux**: Use `sudo python3 app.py`

### Performance Considerations
- **Memory Usage**: Stores up to 2000 packets in RAM (configurable)
- **CPU Load**: Light background packet processing
- **Network Impact**: Non-intrusive packet capture

### Network Privacy
- Only captures traffic from the local machine's network interfaces
- Does not decrypt HTTPS or encrypted traffic
- For educational and authorized testing only

---

## 🐛 Troubleshooting

### Issue: Port Already in Use
```bash
# Change port in app.py or kill process using port 5000
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# macOS/Linux
lsof -i :5000
kill -9 <PID>
```

### Issue: Permission Denied (Scapy)
```bash
# Ensure admin/root privileges
# Windows: Run as Administrator
# macOS/Linux: Use sudo
```

### Issue: Module Not Found
```bash
# Reinstall dependencies
pip install --upgrade flask scapy
```

### Issue: No Packets Captured
- Ensure proper admin/root privileges
- Check network interfaces are active
- Verify firewall settings aren't blocking capture

---

## 📊 API Endpoints

### GET `/`
Dashboard page (requires login)

### POST `/login`
User authentication endpoint

### GET `/logout`
Clear session and return to login

### GET `/data`
Fetch captured packets with filtering
```
Parameters:
  protocol: TCP, UDP, ICMP, or ALL
  category: HTTP, HTTPS, DNS, OTHER, or ALL
  limit: Max packets to return (default: 200)
```

### GET `/export_pcap`
Download captured packets as PCAP file

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Ways to Contribute
- 🐛 Report bugs and issues
- 💡 Suggest new features
- 🔧 Submit code improvements
- 📚 Improve documentation
- 🎨 Enhance UI/UX

---

## 📝 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Mandar Kajbaje**

Made with ❤️ for the cybersecurity community

---

## 📞 Support

For issues, questions, or suggestions:
- 📧 Email: [your-email@example.com]
- 🐙 GitHub Issues: [Create an issue](https://github.com/yourusername/network-sniffer/issues)
- 💬 Discussions: [Join the discussion](https://github.com/yourusername/network-sniffer/discussions)

---

## ⚠️ Disclaimer

This tool is intended for **educational and authorized network testing only**. 

- Unauthorized network monitoring is illegal in most jurisdictions
- Always obtain proper authorization before using this tool
- The authors are not responsible for misuse or damage caused

---

## 🙏 Acknowledgments

- Flask framework for web application
- Scapy for packet manipulation
- Chart.js for data visualization
- CodeAlpha for the internship opportunity

---

<div align="center">

**Made with ❤️ by Mandar Kajbaje**

⭐ Star this repository if you find it useful!

</div>
