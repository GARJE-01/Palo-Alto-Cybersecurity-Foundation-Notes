# Topic 15: Cryptomining (Cryptojacking Attack)

> Unauthorized use of computing resources to generate cryptocurrency
> 

---

## 🧠 SIMPLE EXPLANATION (DEEP)

### What is Cryptomining?

**Cryptomining** = 👉 Using computer power to generate cryptocurrency (like Bitcoin)

#### Normally:

- User mines crypto willingly
- Has permission
- Knows what's happening

#### In Cybersecurity (Cryptojacking):

🔥 **Cryptojacking** = attacker secretly uses your system to mine crypto

---

## 🔥 CORE IDEA

### The Attack Flow:

**Attacker** 👉 Installs malware 👉 Uses your:

- CPU (processing power)
- RAM (memory)
- Power (electricity)

👉 To earn money 💰 **WITHOUT your knowledge**

---

## 🌍 REAL-WORLD EXAMPLE

### You Notice These Signs:

- 🐢 Laptop becoming slow
- 🔊 Fan always running
- 🔋 Battery draining fast
- ❄️ System overheating

### Reason:

👉 Cryptomining malware running in background

---

## ⚙️ HOW ATTACK HAPPENS (STEP-BY-STEP)

### Attack Lifecycle:

**Step 1: Infection**

- User clicks malicious link
- Downloads infected file
- Opens compromised email attachment

**Step 2: Installation**

- Malware gets installed silently
- Often disguised as legitimate software
- May bypass antivirus

**Step 3: Execution**

- System starts mining crypto
- Uses available CPU resources
- Runs continuously in background

**Step 4: Monetization**

- Attacker earns cryptocurrency
- Sends mined coins to attacker's wallet
- Continuous passive income

**Step 5: Concealment**

- User doesn't know
- Malware hides from task manager
- Appears as legitimate process

---

## ❓ WHY ATTACKERS USE THIS

### 🔴 1. STEALTH

- **No visible damage** to system
- **No data theft** (nothing to trace)
- User may not notice for weeks/months
- 👉 Silent attack = harder to detect

### 🟢 2. MONETIZATION

- Easy way to earn money
- Continuous passive income
- No need to sell stolen data
- Direct crypto conversion

### 🟡 3. LOW RISK

- Less detectable than ransomware
- No direct confrontation with user
- Can run indefinitely
- Difficult to attribute to attacker

### 🟠 4. SCALABILITY

- Infect many systems = more mining power
- Botnet with thousands of victims
- Exponential income growth

---

## 🔑 KEY TERMS

| Term | Definition |
| --- | --- |
| **Cryptojacking** | Unauthorized cryptocurrency mining on victim's device |
| **Mining** | Solving complex mathematical problems to generate crypto |
| **CPU Usage** | Percentage of processor power being used |
| **Hash** | Cryptographic output from mining algorithm |
| **Wallet** | Digital address where cryptocurrency is stored |
| **Botnet** | Network of infected computers controlled by attacker |
| **Stratum Protocol** | Mining protocol used for pool mining |

---

## ⚠️ WHY THIS IS DANGEROUS

### Impact on Victim:

| Issue | Description |
| --- | --- |
| 🐢 **Performance** | System becomes extremely slow |
| 🔥 **Overheating** | Hardware works at maximum capacity |
| 🔋 **Power Usage** | Electricity bills increase significantly |
| ⚙️ **Hardware Damage** | CPU/GPU can be damaged over time |
| 📉 **Productivity Loss** | Work becomes difficult or impossible |
| 🔌 **Battery Drain** | Laptops die quickly |

### Why It's Hard to Detect:

- Malware hides from antivirus
- Appears as legitimate process
- No obvious symptoms initially
- Can spread through network

---

## 🎯 HOW CRYPTOJACKING WORKS

### Infection Vectors:

#### 1. Malware Download

- Trojan/worm
- Suspicious software
- Compromised website

#### 2. Browser-based

- Malicious script injected into website
- Runs in browser while user visits
- No installation needed

#### 3. Email Attachment

- Infected file sent via email
- User opens attachment
- Malware executes

#### 4. Network Propagation

- Worm spreads via network
- Infects multiple systems
- Creates botnet

---

## 🔍 HOW TO DETECT

### Signs of Cryptojacking:

#### System Performance:

- [ ]  High CPU usage (80-100%)
- [ ]  Slow applications
- [ ]  Frequent freezing/lag
- [ ]  Computer crashes

#### Hardware Indicators:

- [ ]  Excessive fan noise
- [ ]  System overheating
- [ ]  Unusual heat from laptop
- [ ]  Reduced battery life

#### Process Monitoring:

- [ ]  Unknown background processes
- [ ]  High CPU-consuming processes
- [ ]  Hidden/suspicious processes
- [ ]  Processes using GPU

### Detection Tools:

```
1. Task Manager (Windows) / Activity Monitor (Mac)
   - Check CPU usage
   - Look for unknown processes

2. Resource Monitor
   - Monitor CPU, memory, disk usage

3. Network Monitor
   - Check suspicious outbound connections

4. Antivirus Software
   - Scan for known cryptomining malware
```

---

## 🛡️ PREVENTION & DEFENSE

### For Users:

✅ **Technical Controls:**

- Install reputable antivirus/anti-malware
- Keep software updated
- Use browser extensions (uBlock, NoScript)
- Disable JavaScript when not needed
- Monitor resource usage regularly

✅ **Safe Practices:**

- Don't click suspicious links
- Don't download files from untrusted sources
- Use VPN on public WiFi
- Regularly check running processes
- Monitor network traffic

### For Organizations:

✅ **Enterprise Solutions:**

- Endpoint Detection & Response (EDR)
- Network monitoring/IDS
- Restrict execution policies
- Block known mining pools
- Monitor outbound traffic
- CPU usage baseline monitoring
- Employee training

---

## 💡 INTERVIEW TIP

### 🔥 Question:

👉 **"What is cryptojacking?"**

### ✅ Best Answer Structure:

**"Cryptojacking is a cyberattack where an attacker secretly uses a victim's computing resources (CPU, GPU) to mine cryptocurrency without their knowledge or consent. The attacker typically infects the system with malware, which then runs mining algorithms in the background while the user remains unaware. This differs from legitimate mining because the user has not authorized it and receives no benefit, while the attacker earns profit from the mined coins."**

### 🎯 Follow-up Answers:

**Q: How is it different from ransomware?**

A: "Ransomware encrypts data and demands payment. Cryptojacking steals computing resources silently. Ransomware is obvious; cryptojacking is hidden."

**Q: Why would an attacker use this instead of stealing data?**

A: "Cryptojacking is lower-risk, doesn't require selling stolen data, and provides continuous passive income. It's less detectable than data theft."

**Q: How would you detect it in your organization?**

A: "Monitor CPU usage, check for unknown processes, monitor network traffic for connections to mining pools, and use EDR solutions."

---

## ⚠️ EXAM TRAP

### ❌ Wrong Thinking:

"No data theft = not dangerous"

### ✅ Correct Understanding:

"Resource misuse = still serious cyberattack"

### Why This Matters:

- CPU damage = long-term impact
- Energy waste = financial loss
- System slowdown = productivity loss
- Still unauthorized access
- Could be entry point for other attacks

---

## 🧠 MEMORY TRICKS

### Acronym: CRYPTO

- **C**ircuit (CPU circuits being used)
- **R**esources (stealing system resources)
- **Y**our (your computer)
- **P**ower (processing power)
- **T**heft (stealing from you)
- **O**utput (cryptocurrency output)

### Quick Phrase:

👉 **"Your CPU = Their Money"**

### Visual Comparison:

```
Legitimate Mining:     Cryptojacking:
✅ User consents       ❌ Secret attack
✅ User benefits       ❌ Only attacker benefits
✅ Transparent         ❌ Hidden malware
✅ Controlled          ❌ Uncontrolled resource use
```

---

## 📊 REAL-WORLD STATISTICS

### Famous Cases:

**1. Monero Mining Botnet (2017)**

- Infected hundreds of thousands of computers
- Distributed through pirated software
- Earned attacker millions

**2. Coinhive Script (2018)**

- Browser-based mining script
- Used on compromised websites
- Affected major websites

**3. Mobile Cryptojacking**

- Android apps with hidden miners
- Drains battery and data
- Hard to detect on mobile

---

## 🧠 QUICK SUMMARY

### One-Sentence Definition:

**Cryptojacking is the unauthorized use of someone's computer to mine cryptocurrency without their knowledge.**

### Key Points:

- ⛏️ **Cryptomining** = generating cryptocurrency (legitimate)
- 🔥 **Cryptojacking** = illegal/unauthorized mining
- 🤫 **Silent** + low risk for attacker
- 💻 **Uses victim's resources** (CPU, power, bandwidth)
- 🚨 **Hard to detect** but causes system degradation
- 💰 **Passive income** for attacker
- ⚠️ **Not data theft** but still serious

---

## 📝 PRACTICE QUESTIONS

### Q1: Definition

**What is the primary difference between legitimate cryptocurrency mining and cryptojacking?**

A) Cryptojacking uses a different algorithm

B) Cryptojacking occurs without user's knowledge or consent

C) Cryptojacking only affects GPUs

D) There is no difference

✅ **Answer: B** - The key difference is authorization and knowledge

### Q2: Detection

**Which of the following is a sign of cryptojacking infection?**

A) Sudden data encryption

B) Excessive CPU usage and system slowdown

C) Missing files

D) Account lockouts

✅ **Answer: B** - Resource exhaustion is the main indicator

### Q3: Risk Assessment

**Why do attackers prefer cryptojacking over ransomware?**

A) It's faster to execute

B) It's more profitable

C) It's harder to detect and lower risk

D) It affects more systems

✅ **Answer: C** - Stealth and low detection risk are key advantages

### Q4: Prevention

**What is the best way to prevent cryptojacking?**

A) Disable antivirus

B) Keep systems updated, use reputable security software, monitor resources

C) Disconnect from internet

D) Use only cloud services

✅ **Answer: B** - Layered defense is most effective

---

## 🔗 CONNECTIONS TO OTHER TOPICS

**Related Topics:**

- Topic 12: Malware (delivery mechanism)
- Topic 8: Types of Threats (resource-based threat)
- Topic 10: Common Wi-Fi Attacks (browser-based variants)
- Topic 14: Wi-Fi Security Best Practices (defense)

---

## 💼 CAREER RELEVANCE

### Where You'll See This:

- **SOC Analyst**: Detecting unusual CPU usage
- **Incident Response**: Investigating slowdown reports
- **Network Security**: Blocking mining pool connections
- **Endpoint Security**: Implementing EDR solutions
- **Threat Intelligence**: Tracking cryptojacking campaigns

---

**Ready to test your knowledge? Review the practice questions and explain cryptojacking to someone else!** 📚