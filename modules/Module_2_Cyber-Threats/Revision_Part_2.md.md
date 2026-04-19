# 📑 Module 2 Part 2 — Revision & Practice

---

## ✅ Part 2 Revision Checklist

- ✅ Wi-Fi Security Basics (authentication and open networks)
- ✅ Wi-Fi Encryption evolution (WEP → WPA → WPA2 → WPA3)
- ✅ Common Wi-Fi Attacks (Evil Twin, Packet Sniffing)
- ✅ Advanced Wi-Fi Attacks (Jasager, SSLStrip)
- ✅ Malware example (Emotet)
- ✅ Insider Wi-Fi Attack (Doppelganger)
- ✅ Wi-Fi Security Best Practices (8 core practices)

---

## 📊 Attack Summary Table

| Attack | Type | Target | How It Works | Defense |
| --- | --- | --- | --- | --- |
| **Evil Twin** | Network spoofing | User Wi-Fi connection | Fake network mimics real | Verify network name |
| **Packet Sniffing** | Data interception | Unencrypted data | Captures network packets | Use encryption (WPA3) |
| **Jasager** | Auto-connection | Device auto-connect | Impersonates known networks | Disable auto-connect |
| **SSLStrip** | MITM attack | HTTPS downgrade | Removes encryption | HSTS, modern browsers |
| **Emotet** | Malware | Network spread | Self-propagating trojan | Email filters, training |
| **Doppelganger** | Device spoofing | MAC address spoofing | Copies device identity | NAC, MAC monitoring |

---

## 📌 Wi-Fi Encryption Comparison

| Protocol | Era | Security | Status | Use |
| --- | --- | --- | --- | --- |
| **WEP** | 2000s | 🔴 Very weak | 퉴c Obsolete | NONE |
| **WPA** | 2003 | 🟡 Weak | ⚠️ Old | Legacy only |
| **WPA2** | 2004+ | 🞫 Strong | ✅ Current | Most networks |
| **WPA3** | 2018+ | 🔵 Very strong | 🔥 Best | New deployments |

---

## ❓ Practice Questions

### Short Answer Questions

1. Why is Wi-Fi security based on authentication?
2. Explain the evolution from WEP to WPA3
3. What is an Evil Twin attack and how does it work?
4. What is packet sniffing and why is it effective?
5. What makes Jasager attack different from Evil Twin?
6. How does SSLStrip downgrade HTTPS to HTTP?
7. How does Emotet spread across networks?
8. What is Doppelganger attack and how does it use MAC addresses?
9. Name 8 Wi-Fi security best practices
10. Why is user training important for Wi-Fi security?

### Scenario-Based Questions

**Scenario 1**: 

You detect duplicate Wi-Fi networks in your office. One is the real network, one is fake. How do you identify which is real?

**Scenario 2**: 

An employee's laptop gets infected with Emotet at home. What's the attack chain once they connect to office Wi-Fi?

**Scenario 3**: 

Your company uses WPA2. A hacker can brute-force it. What should you upgrade to?

**Scenario 4**: 

You observe a device connecting with MAC address of a trusted laptop. How could this be Doppelganger attack?

**Scenario 5**: 

Employee connects to "Airport_Free_WiFi" at airport. How would Jasager attack work here?

---

## 📊 Attack Lifecycle Comparison

### **Evil Twin**

1. Create fake network with same SSID
2. Wait for user to connect
3. Intercept all traffic
4. Steal credentials/data

### **Jasager**

1. Listen for beacon requests
2. Automatically respond to known networks
3. Force auto-connection
4. Intercept traffic silently

### **SSLStrip**

1. Intercept HTTPS request
2. Downgrade to HTTP
3. Show fake security lock
4. Capture data in plaintext

### **Emotet**

1. Infect initial system (phishing)
2. Scan Wi-Fi networks
3. Brute-force Wi-Fi passwords
4. Spread to connected systems
5. Establish C2 control

### **Doppelganger**

1. Observe legitimate device MAC
2. Spoof MAC address
3. Connect to network
4. Gain trusted device access

---

## 🛰️ 8 Core Security Practices Summary

```
🔐 Encryption: Use WPA3
🔏 Strong Passwords: Complex, long, unique
🛳 No Open Wi-Fi: Always require authentication
🛰 MFA: Password + second factor
🔍 Monitor: Track devices and traffic
📊 Segment: Separate networks
🔄 Update: Regular patches
👥 Train: User awareness
```

---

## 💡 Key Interview Questions & Answers

### Q1: "What is the difference between WPA2 and WPA3?"

**A**: "WPA3 is stronger than WPA2. It offers better protection against brute-force attacks, individual session encryption, and improved overall security. WPA2 is still secure but WPA3 is recommended."

### Q2: "What is Evil Twin attack?"

**A**: "It's a rogue Wi-Fi network with the same SSID as a legitimate one. Users unknowingly connect to it, allowing attackers to see all traffic and steal credentials."

### Q3: "How would you defend against Jasager?"

**A**: "Disable auto-connect on devices, manually verify Wi-Fi networks, use MAC randomization, and educate users to verify network details."

### Q4: "What makes SSLStrip dangerous?"

**A**: "It downgrades HTTPS to HTTP, making users think they're on a secure connection when they're actually not. This allows plaintext capture of credentials."

### Q5: "How does Emotet spread?"

**A**: "It infects a system via phishing, then scans nearby Wi-Fi networks, brute-forces passwords, and spreads to other connected devices automatically."

---

## 💻 Wi-Fi Attack Mitigation Strategies

### **Against Evil Twin**

- Verify network names carefully
- Check for duplicate networks
- Use public lists of real networks
- Never auto-connect

### **Against Packet Sniffing**

- Use WPA3 encryption
- Use HTTPS for websites
- Avoid public Wi-Fi for sensitive activities
- Use VPN on public networks

### **Against Jasager**

- Disable Wi-Fi auto-connect
- Manually select networks
- Use MAC address randomization
- Monitor connection behavior

### **Against SSLStrip**

- Use HSTS headers (HTTP Strict Transport Security)
- Use modern browsers (prevent downgrade)
- Verify lock icon validity
- Use certificate pinning

### **Against Emotet**

- Email filtering and detection
- Network monitoring for C2
- User training on phishing
- Segmented networks
- Regular patching

### **Against Doppelganger**

- Network Access Control (NAC)
- MAC address monitoring
- Certificate-based auth
- Port security
- DHCP snooping

---

## 🔟 Exam & Interview Focus

**Most Important Topics**:

1. **WPA3 vs WPA2** ← Encryption knowledge
2. **Evil Twin** ← Common attack
3. **Packet Sniffing** ← Data protection
4. **Emotet** ← Real malware example
5. **Best Practices** ← Defense strategies
6. **Doppelganger** ← Advanced topic

---

## 🚀 Quick Memory Aids

**Encryption Timeline**: "WEP is broken, WPA is weak, WPA2 is solid, WPA3 is gold"

**Common Attacks**: "Fake Wi-Fi, Data sniff, Auto-connect, Downgrade HTTPS"

**Best Practices**: "Encrypt – Strong Pass – Monitor – Update – Train – Segment"

**Attack Types**: "Network spoofing, Data interception, MITM attacks, Malware spread"

---

## 🎯 Part 2 Summary Card

| Aspect | Key Takeaway |
| --- | --- |
| **Encryption** | WEP broken, WPA2 common, WPA3 best |
| **Common Attacks** | Evil Twin, Packet Sniffing (both on unencrypted) |
| **Advanced Attacks** | Jasager (auto-connect), SSLStrip (HTTPS downgrade) |
| **Malware** | Emotet spreads via Wi-Fi networks |
| **Insider Attack** | Doppelganger (MAC spoofing) |
| **Defense** | Layered security (encryption, monitoring, training) |
| **Best Practice** | Multiple layers ≠ single solution |

---

## 🚨 Red Flags to Watch

**Network Red Flags**:

- Duplicate network names
- Unexpected devices connecting
- Unusual traffic patterns
- Failed authentication attempts
- Devices connecting from impossible locations

**Malware Red Flags**:

- Unusual network scanning
- C2 communication attempts
- Password cracking attempts
- Lateral movement patterns

---

## 🎉 Module 2 Complete Summary

**Part 1**: Attackers, motivations, attack lifecycle, MITRE, real cases

**Part 2**: Wi-Fi attacks, encryption, malware, defenses

**Total Topics**: 14 comprehensive topics

**Key Skills**: Identify attacks, understand defenses, apply layered security