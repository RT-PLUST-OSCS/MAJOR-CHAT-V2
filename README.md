
# 🔐 MAJOR Chat V2 - Military-Grade Secure Messaging

## 🎯 Quick Start (30 Seconds) 
```bash
# 1. Install & Run
pip install flask && python app.py

# 2. Open browser
# http://localhost:5000
```

## 📋 Table of Contents
1. [Features](#-features)
2. [Installation](#-installation)
3. [Basic Usage](#-basic-usage)
4. [Cloudflare Tunnel Setup](#☁️-cloudflare-tunnel-setup)
5. [Advanced Configuration](#⚙️-advanced-configuration)
6. [Security Features](#🛡️-security-features)
7. [FAQ](#❓-faq)
8. [Contributing](#🤝-contributing)

## ✨ Features
| Feature | Description | Icon |
|---------|-------------|------|
| **On-Demand** | Start/stop anytime, no permanent server | ⚡ |
| **Zero Storage** | Messages disappear after closing | 🗑️ |
| **IP Protection** | Hide your real IP with Cloudflare | 🛡️ |
| **No Login** | Start chatting immediately | 🚪 |
| **Secure Sharing** | Invite via secure links | 🔗 |
| **Open Source** | MIT Licensed, fully transparent | 🔓 |

## 📥 Installation

### Prerequisites
- Python 3.7+
- pip package manager

### Step-by-Step Installation
```bash
# Clone repository
git clone https://github.com/yourusername/MAJOR-Chat.git
cd MAJOR-Chat

# Install requirements
pip install -r requirements.txt

# Run MAJOR Chat
python app.py
```

## 🚀 Basic Usage

### Starting the Chat Server
```bash
# Default port (5000)
python app.py

# Custom port
python app.py --port 8080
```

### Accessing the Chat
1. **Open your browser**
2. **Navigate to:** `http://localhost:5000`
3. **Start chatting immediately**

### Sharing Locally
- Share this link with others on your network:
  ```
  http://YOUR_LOCAL_IP:5000
  ```
- Find your local IP:
  ```bash
  # Windows
  ipconfig

  # Linux/Mac
  ifconfig
  ```

## ☁️ Cloudflare Tunnel Setup

### Why Use Cloudflare Tunnel?
- ✅ **Hide your IP address**
- ✅ **Get HTTPS automatically**
- ✅ **No port forwarding required**
- ✅ **Free & easy to set up**

### Installation Steps

#### Step 1: Download Cloudflared
```bash
# Windows (PowerShell as Admin)
Invoke-WebRequest -Uri "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.exe" -OutFile "cloudflared.exe"

# Linux
wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64
chmod +x cloudflared
sudo mv cloudflared /usr/local/bin/

# Mac
brew install cloudflared
```

#### Step 2: Start MAJOR Chat
```bash
# Make sure MAJOR Chat is running on port 5000
python app.py
# Server starts at: http://localhost:5000
```

#### Step 3: Create Cloudflare Tunnel
```bash
# Open NEW terminal window
# Run this command:
cloudflared tunnel --url http://localhost:5000

# For custom port:
cloudflared tunnel --url http://localhost:8080
```

#### Step 4: Get Your Secure Link
After running cloudflared, you'll see:
```
✅ Your tunnel is ready! Connect with:
https://random-name.trycloudflare.com
```

**Share this link securely!** It provides:
- 🔒 HTTPS encryption
- 🌍 Global accessibility
- 🛡️ IP protection

### One-Command Solution (Advanced)
```bash
# Start both MAJOR Chat and Cloudflare Tunnel
python app.py & cloudflared tunnel --url http://localhost:5000
```

## ⚙️ Advanced Configuration

### Using Different Ports
```bash
# Run on port 8080
python app.py --port 8080

# Connect Cloudflare to port 8080
cloudflared tunnel --url http://localhost:8080
```

### Running in Background
```bash
# Linux/Mac
python app.py > chat.log 2>&1 &
cloudflared tunnel --url http://localhost:5000 > tunnel.log 2>&1 &

# Windows (PowerShell)
Start-Process python -ArgumentList "app.py" -WindowStyle Hidden
Start-Process cloudflared -ArgumentList "tunnel --url http://localhost:5000" -WindowStyle Hidden
```

### Permanent Tunnel (With Cloudflare Account)
1. **Create free Cloudflare account**
2. **Login to cloudflared:**
   ```bash
   cloudflared tunnel login
   ```
3. **Create named tunnel:**
   ```bash
   cloudflared tunnel create major-chat
   cloudflared tunnel route dns major-chat chat.yourdomain.com
   cloudflared tunnel run major-chat
   ```

## 🛡️ Security Features

### Built-in Security
- 🔐 **No message persistence** - Everything is volatile
- 🌐 **Local-first design** - No external dependencies
- 🧹 **Auto-cleanup** - Regular memory cleaning
- 🚫 **No tracking** - No analytics or logging

### Security Best Practices
1. **Always use HTTPS** when sharing links
2. **Restart the server** after sensitive conversations
3. **Use strong passwords** if adding authentication
4. **Monitor active connections** regularly

## ❓ FAQ

### Q: Is my data stored anywhere?
**A:** No! All messages exist only in memory and disappear when you close the app.

### Q: Can I use this for team communication?
**A:** Yes! Perfect for temporary team meetings or sensitive discussions.

### Q: Is Cloudflare Tunnel free?
**A:** Yes, completely free for personal use with generous limits.

### Q: What if cloudflared disconnects?
**A:** Just restart it. Your chat continues running locally.

### Q: Can I customize the interface?
**A:** Yes! Edit files in `templates/` and `static/` folders.

## 🤝 Contributing

We welcome contributions! Here's how:

1. **Fork the repository**
2. **Create a feature branch**
3. **Make your changes**
4. **Submit a Pull Request**

### Quick Contribution Guide
```bash
# 1. Fork & Clone
git clone https://github.com/YOUR_USERNAME/MAJOR-Chat.git

# 2. Create branch
git checkout -b feature/awesome-feature

# 3. Make changes & commit
git add .
git commit -m "Add awesome feature"

# 4. Push & PR
git push origin feature/awesome-feature
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## ⭐ Star History
If you find MAJOR Chat useful, please consider giving it a star on GitHub!

## 🚀 Quick Reference Card

```bash
# Most common commands
pip install flask                    # Install dependencies
python app.py                        # Start local chat
cloudflared tunnel --url http://localhost:5000  # Secure sharing
```

---
**Built with ❤️ for secure, private, and temporary communications**
```
