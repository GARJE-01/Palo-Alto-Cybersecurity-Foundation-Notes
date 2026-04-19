# Topic 13: Insider Wi-Fi Attack — Doppelganger Attack

## 📌 Definition

Doppelganger Attack is an **insider-type attack** where an attacker **spoofs the identity of a legitimate device** to gain unauthorized network access without being detected.

---

## 🧠 Simple Explanation

**Unlike other attacks**:

- NOT a fake Wi-Fi network
- NOT external attacker
- NOT phishing email

**Instead**: Attacker **copies the identity of a trusted device** already on the network.

---

## 📌 What is Device Identity?

Every network device has a unique identifier: **MAC Address**

**Example MAC Address**: `00:1A:2B:3C:4D:5E`

Network security systems trust devices based on MAC address.

---

## ⚙️ How Doppelganger Attack Works (Step-by-Step)

### **Stage 1: Reconnaissance**

- Attacker observes network
- Identifies legitimate devices
- Notes MAC addresses
- Identifies trusted devices

### **Stage 2: Copy Identity**

- Attacker finds a legitimate device (e.g., employee laptop)
- Records its MAC address: `00:1A:2B:3C:4D:5E`
- Changes their device MAC to match
- Now appears identical to legitimate device

### **Stage 3: Connection Request**

- Attacker's device sends connection request
- Uses spoofed MAC address
- Network sees MAC address it recognizes

### **Stage 4: Network Trust**

- Network thinks: "This MAC address is trusted"
- Thinks it's the legitimate device
- Grants access automatically

### **Stage 5: Unauthorized Access**

- Attacker now on network
- Can access resources
- Can move to other systems
- Can steal data

---

## 🌍 Real-World Example: Office Attack

**Scenario**:

1. Employee's laptop (MAC: `AA:BB:CC:DD:EE:FF`) connected to office Wi-Fi
2. Attacker observes network, finds this MAC
3. Attacker spoofs their device with same MAC
4. Attacker's device connects to Wi-Fi
5. Network thinks it's the employee's laptop
6. Attacker gains full access
7. Employee and attacker both connected as "same device"
8. Attacker can:
    - Access network drives
    - Steal files
    - Install malware
    - Conduct internal attacks

---

## 🔴 Why This Attack is Dangerous

### **Looks Like Internal User**

- Network trusts device by MAC
- Appears as legitimate employee device
- Passes basic authentication

### **Hard to Detect**

- Network sees known MAC address
- Traffic appears normal
- No external connection signs
- Blends with legitimate traffic

### **Bypasses Some Security**

- Skips initial network authentication
- May bypass MAC filtering
- Assumes device is trustworthy

### **Inside Network Access**

- Can access internal resources
- Can perform lateral movement
- Can access shares and servers
- Can steal sensitive data

---

## 🔑 Key Terms

| Term | Definition |
| --- | --- |
| **MAC Address** | Unique hardware identifier for network devices |
| **Spoofing** | Faking identity of another device |
| **DHCP** | Protocol that assigns IP addresses |
| **ARP** | Protocol for mapping IP to MAC |
| **Doppelganger** | "Double-ganger" (look-alike) |

---

## ⚖️ Comparison: Evil Twin vs. Doppelganger

| Aspect | Evil Twin | Doppelganger |
| --- | --- | --- |
| **Type** | External fake network | Internal device spoofing |
| **Victim action** | Must connect to fake network | No action needed |
| **Target** | Network entry | Trusted device identity |
| **What's spoofed** | Network name (SSID) | Device identity (MAC) |
| **Detection** | Can see duplicate networks | Very hard to detect |
| **Impact** | Traffic interception | Internal network access |

---

## 💡 Exam & Interview Points

**Question**: *"What is Doppelganger attack?"*

**Best answer**:

> "Doppelganger is an insider attack where an attacker spoofs the MAC address of a legitimate device to appear as a trusted network member. This bypasses network authentication and allows unauthorized access to internal resources."
> 

**Key points to mention**:

- MAC address spoofing
- Mimics legitimate device
- Difficult to detect
- Assumes device is trusted
- Works on networks with MAC-based security

---

## ⚠️ Common Exam Trap

**Wrong thinking**:

- ❌ "Confusing Evil Twin and Doppelganger attacks"
- ❌ "Both are external attacks"

**Correct understanding**:

- ✅ **Evil Twin**: External fake Wi-Fi network
- ✅ **Doppelganger**: Internal device spoofing
- ✅ Both gain network access, different methods

---

## 🛰️ Defense Against Doppelganger

**Network Controls**:

- Network Access Control (NAC)
- Certificate-based authentication
- Port security
- Monitoring for duplicate MACs
- DHCP snooping
- Dynamic ARP inspection

---

## 🚀 Quick Revision

- ▪ **Type**: Insider attack (device spoofing)
- ▪ **Method**: Copy MAC address of trusted device
- ▪ **Target**: Network access
- ▪ **Detection**: Difficult (looks legitimate)
- ▪ **Impact**: Full internal network access
- ▪ **Prevention**: MAC authentication, NAC, monitoring
- ▪ **Memory trick**: "Copy Identity → Become Trusted → Access Network"