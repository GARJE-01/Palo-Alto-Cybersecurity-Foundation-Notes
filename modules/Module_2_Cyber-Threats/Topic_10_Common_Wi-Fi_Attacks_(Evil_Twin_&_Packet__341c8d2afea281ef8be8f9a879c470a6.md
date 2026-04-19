# Topic 10: Common Wi-Fi Attacks (Evil Twin & Packet Sniffing)

## 🧠 Simple Explanation

Wi-Fi attacks happen when attackers **exploit weak or open networks** to intercept data or gain unauthorized access.

Two very common attacks:

1. **Evil Twin Attack** (fake network)
2. **Packet Sniffing** (data interception)

---

## 🔴 Common Wi-Fi Attack #1: Evil Twin Attack

### 📌 Definition

A fake Wi-Fi network that mimics a legitimate one to trick users into connecting.

### 🧠 How It Works

Attacker creates:

- Same network name (SSID)
- Same appearance as real network
- Slightly stronger signal

Users think they're connecting to legitimate network.

### 🌍 Real-World Example

**Airport scenario**:

- Real Wi-Fi: "Airport_Free_WiFi"
- Fake Wi-Fi: "Airport_Free_WiFi" (created by attacker)
- User connects to fake one without knowing

### ⚙️ What Happens After Connection

Once user connects to Evil Twin:

- Attacker sees ALL traffic
- Can steal:
    - Passwords
    - Bank details
    - Emails
    - Credit card numbers
    - Private messages

### ❓ Why It Matters

- User THINKS they're on safe network
- Actually attacker controls everything
- No encryption means data is visible
- Very difficult to detect

### 🔑 Key Terms

| Term | Definition |
| --- | --- |
| **SSID** | Wi-Fi network name |
| **Access Point (AP)** | Physical Wi-Fi device |
| **Rogue AP** | Fake/malicious access point |
| **Man-in-the-Middle (MITM)** | Attacker between user and real network |

### 💡 Interview Points

**Question**: *"What is Evil Twin attack?"*

**Best answer**:

> "It's a rogue Wi-Fi network with the same SSID as a legitimate network. Users unknowingly connect to it, allowing attackers to see all their traffic, steal credentials, and intercept data."
> 

---

## 🔵 Common Wi-Fi Attack #2: Packet Sniffing

### 📌 Definition

Capturing and analyzing network data packets to extract sensitive information.

### 🧠 How It Works

**On unencrypted networks**:

1. User sends data (login, message, etc.)
2. Data broken into "packets" (small units)
3. Attacker's tool captures these packets
4. Attacker analyzes and reads the content

### 🌍 Real-World Example

**Café with open Wi-Fi**:

1. You log into email
2. Your username and password sent as packets
3. Attacker's packet sniffer captures them
4. Attacker reads your credentials

### ⚙️ What Attacker Can See

Without encryption:

- Login credentials (username/password)
- Email messages
- Chat messages
- Browsing activity
- Credit card numbers
- Bank details

### ❓ Why It Matters

- Works on unencrypted networks
- Easy to perform (simple tools)
- User has NO idea they're being monitored
- Data is visible in plaintext

### 🔑 Key Terms

| Term | Definition |
| --- | --- |
| **Packet** | Small unit of data sent over network |
| **Sniffer** | Tool that captures network packets |
| **Plaintext** | Unencrypted data (readable) |
| **Wireshark** | Common packet sniffing tool |

### 💡 Interview Points

**Question**: *"What is packet sniffing?"*

**Best answer**:

> "It's the process of capturing and analyzing network packets to extract sensitive information like passwords, messages, and browsing activity. It works especially well on unencrypted networks."
> 

---

## ⚖️ Comparison: Evil Twin vs. Packet Sniffing

| Aspect | Evil Twin | Packet Sniffing |
| --- | --- | --- |
| **Setup** | Create fake network | Listen on existing network |
| **User action** | Must connect to fake AP | No user action needed |
| **How data stolen** | All traffic routed through attacker | Packets captured from air |
| **Detection** | Can see network appears twice | Hard to detect (passive) |
| **Difficulty** | Medium | Easy |
| **Defense** | Check network name carefully | Use encryption (HTTPS/WPA3) |

---

## ⚠️ Common Exam Trap

**Wrong thinking**:

- ❌ "I'm on Wi-Fi so my data is safe"

**Correct understanding**:

- ✅ "Open or weak Wi-Fi = data easily stolen"
- ✅ "Encryption is essential"
- ✅ "Must verify network name"

---

## 🚀 Quick Revision

- ▪ **Evil Twin**: Fake Wi-Fi network mimicking real one
- ▪ **Packet Sniffing**: Capturing data from network
- ▪ **Both attacks**: Easier on unencrypted networks
- ▪ **Prevention**: Use WPA3, verify network name, use HTTPS
- ▪ **Detection**: Check for duplicate networks, monitor traffic
- ▪ **Memory trick**: "Fake Network → Connect → Capture Data"