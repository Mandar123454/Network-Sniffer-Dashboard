# Network Sniffer Dashboard - Setup & Run Instructions

## ⚠️ IMPORTANT: Administrator Privileges Required

**Packet sniffing requires elevated privileges!** You MUST run this application as **Administrator** (Windows) or with **sudo** (Linux) to capture network packets.

### Why Admin Privileges?
- Scapy needs access to raw network sockets
- Network interfaces require CAP_NET_RAW capability
- Without admin rights, packet capture will silently fail (app still runs, but shows 0 packets)

---

## Running on Windows (VS Code)

### Option 1: Run VS Code as Administrator (Recommended for Development)
1. **Close VS Code completely**
2. **Right-click** on VS Code shortcut
3. Select **"Run as administrator"**
4. Open your project folder
5. Open Terminal in VS Code
6. Run: `python app.py`

### Option 2: Run Terminal as Administrator
1. **Press** `Win + R`
2. Type: `cmd`
3. **Right-click** → **Run as administrator**
4. Navigate to project: `cd "e:\Internships and Projects\CyberSecurity CodeAlpha Internship\Internship Work\Projects\Network Sniffer"`
5. Activate venv: `.\.venv\Scripts\Activate.ps1`
6. Run: `python app.py`

---

## Running on Linux / macOS

```bash
# Activate virtual environment
source venv/bin/activate

# Run with sudo (packet capture requires root)
sudo python app.py

# Or use sudo with full path
sudo /path/to/venv/bin/python app.py
```

---

## Access the Dashboard

Once running:
- **URL**: http://localhost:5000
- **Login**: 
  - Username: `admin`
  - Password: `admin123`
- **Start capturing packets** and view real-time statistics

---

## What You'll See

### ✅ With Admin Privileges
- Live packet capture starts immediately
- Displays protocol statistics (TCP, UDP, ICMP, etc.)
- Shows packet size trends
- Allows export to PCAP and CSV

### ❌ Without Admin Privileges
- App runs successfully
- Dashboard loads
- **BUT**: "Total Packets Captured: 0" (no data captured)
- Export buttons show "No packets to export"

---

## Troubleshooting

### "Permission Denied" Error
**Solution**: Run as administrator (see instructions above)

### Port 5000 Already in Use
**Solution**: Change the port:
```bash
set WEBSITES_PORT=8000
python app.py
```

### Still No Packets Showing?
1. Verify you're running as administrator
2. Check if firewall is blocking
3. Ensure Scapy is installed: `pip install scapy`
4. Try a different network interface (advanced users)

---

## Environment Variables (Optional)

```bash
# Custom port
set WEBSITES_PORT=5000

# Custom credentials
set USERNAME=myuser
set PASSWORD=mypass123

# Debug mode
set FLASK_ENV=development
```

---

## Cloud Deployment Notes

**Azure App Service cannot capture live packets** because:
- No raw socket privileges in managed containers
- Network interfaces are isolated
- Security restrictions prevent CAP_NET_RAW

**This application is designed for local network analysis, not cloud deployment.**

---

## Features

- 🔍 Real-time packet capture & analysis
- 📊 Protocol distribution charts
- 🔎 Filter by protocol & category
- 💾 Export to PCAP (Wireshark compatible)
- 📋 Export to CSV (Excel compatible)
- 🔐 Simple authentication
- 🎨 Beautiful dark-themed dashboard

---

## Login Credentials

```
Default:
  Username: admin
  Password: admin123
```

Change these in `.env` file or environment variables.

---

**Happy packet sniffing! 🎯**
