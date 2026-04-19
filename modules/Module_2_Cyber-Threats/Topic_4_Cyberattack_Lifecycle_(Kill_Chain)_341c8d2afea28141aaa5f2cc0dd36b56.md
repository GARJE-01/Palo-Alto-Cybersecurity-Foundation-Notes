# Topic 4: Cyberattack Lifecycle (Kill Chain)

## 📌 Definition

A structured, step-by-step process that attackers follow to compromise systems and achieve their objectives. Also called the **"Kill Chain."**

---

## 🧠 Core Concept

A cyberattack does NOT happen in one step — it follows a **7-stage structured process** like a planned operation.

**Critical insight**: Stopping ANY ONE stage prevents the entire attack.

---

## ⚙️ The 7-Stage Cyberattack Lifecycle

### 🔎 **Stage 1: Reconnaissance (Information Gathering)**

**What happens**: Attacker collects information about target

- Research employees on LinkedIn
- Identify email addresses
- Map network systems
- Find vulnerabilities

**Real example**: Checking employee LinkedIn profiles to target phishing

**Why it matters**: Attack planning starts here

---

### 🛠️ **Stage 2: Weaponization (Preparing Attack)**

**What happens**: Attacker prepares the attack tools

- Creates malware code
- Embeds virus in file (PDF, Word, Excel)
- Packages exploit code
- Tests payload

**Real example**: Creating infected email attachment

**Why it matters**: Attack infrastructure is built here

---

### 📩 **Stage 3: Delivery (Sending Attack)**

**What happens**: Attack is delivered to victim

- Phishing email with malicious link
- Compromised website
- USB drive
- File sharing

**Real example**: Phishing email with weaponized attachment

**Why it matters**: Entry point of attack

---

### 💥 **Stage 4: Exploitation (Triggering Attack)**

**What happens**: Victim interacts with attack

- User clicks link
- Opens file
- Visits compromised site
- Runs executable

**Real example**: Employee clicks fake email link

**Why it matters**: System gets compromised at this point

---

### 📥 **Stage 5: Installation (Establishing Persistence)**

**What happens**: Attacker installs tools on system

- Malware installed
- Backdoor created
- Remote access tool deployed
- Persistence mechanism set

**Real example**: Trojan malware installed silently

**Why it matters**: Attacker gains stable foothold

---

### 🎮 **Stage 6: Command & Control (C2/C&C)**

**What happens**: Attacker establishes control

- Sends commands to infected system
- Controls system remotely
- Receives data from system
- Maintains connection

**Real example**: Hacker remotely controlling infected PC

**Why it matters**: Full control achieved — attacker can now act

---

### 🎯 **Stage 7: Actions on Objectives (Final Goal)**

**What happens**: Attacker achieves their goal

- Data theft/exfiltration
- Ransomware deployment
- System damage/deletion
- Lateral movement for more access

**Real example**: Stealing customer database

**Why it matters**: Actual damage/harm happens here

---

## 📊 Complete Flow Chart

```
Reconnaissance → Weaponization → Delivery → Exploitation → 
Installation → Command & Control → Actions on Objectives
```

---

## 🌍 Real-World Complete Example: Phishing Attack

| Stage | Action |
| --- | --- |
| **Recon** | Collect employee emails from LinkedIn |
| **Weapon** | Create fake login page |
| **Delivery** | Send phishing email |
| **Exploit** | User clicks link and enters credentials |
| **Install** | Access system using stolen credentials |
| **C2** | Attacker maintains remote access |
| **Action** | Steal sensitive company data |

---

## ❗ MOST IMPORTANT CONCEPT

**You DO NOT need to stop all 7 stages.**

**STOPPING ANY ONE STAGE = Attack fails completely**

For example:

- ✅ Block delivery email → Attack stops
- ✅ Prevent exploitation (patch system) → Attack stops
- ✅ Detect C2 communication → Attack stops

---

## 🔑 Key Terms

| Term | Definition |
| --- | --- |
| **Exploit** | Using vulnerability to compromise system |
| **Payload** | Malicious code/tool delivered |
| **C2 (Command & Control)** | Attacker communication with infected system |
| **Kill Chain** | Same as cyberattack lifecycle |
| **Persistence** | Maintaining access after initial compromise |

---

## 💡 Exam & Interview Points

**Very common question**: *"Explain the cyberattack lifecycle"*

**Best answer**:

> "A cyberattack follows 7 stages: reconnaissance, weaponization, delivery, exploitation, installation, command & control, and actions on objectives. Breaking any one stage can prevent the entire attack."
> 

**Key points to mention**:

- It's a structured process (not random)
- Attacker must complete each stage sequentially
- Breaking any stage stops the attack
- Different defenses target different stages

---

## ⚠️ Common Exam Trap

**Wrong**: Students assume all stages must be stopped

**Correct**: Stopping even ONE stage defeats the attack

---

## 🚀 Quick Revision

- ▪ **7 stages in order**: Recon → Weapon → Deliver → Exploit → Install → C2 → Action
- ▪ **Sequential process**: Must follow order
- ▪ **Stop any stage**: Breaks entire attack
- ▪ **Memory aid**: "R-W-D-E-I-C-A"
- ▪ **Real-world relevance**: Every security control targets one of these stages