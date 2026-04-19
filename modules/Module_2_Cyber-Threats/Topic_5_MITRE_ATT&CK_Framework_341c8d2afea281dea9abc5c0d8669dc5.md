# Topic 5: MITRE ATT&CK Framework

## 📌 Definition

A **framework for categorizing attacker behavior** in real-world cyberattacks. Instead of just saying "system is hacked," MITRE helps answer:

- **How** did attacker enter?
- **What techniques** did they use?
- **What is** their goal?

---

## 🧠 Core Concept

MITRE breaks attacks into three layers:

### 🔹 **1. Tactics (WHY)**

What the attacker wants to achieve

**Examples**:

- Credential access
- Data theft
- Persistence
- Defense evasion

### 🔹 **2. Techniques (HOW)**

How the attacker achieves the tactic

**Examples**:

- Phishing
- Password cracking
- Malware installation
- Privilege escalation

### 🔹 **3. Procedures (REAL METHOD)**

Actual implementation in real attack

**Example**: Using PowerShell script to steal Windows passwords

---

## 🌍 Real-World Example: Password Theft

| Layer | Description |
| --- | --- |
| **Tactic** | Credential Access (WHY — attacker needs login creds) |
| **Technique** | Password Dumping (HOW — extract password hashes) |
| **Procedure** | Using Mimikatz tool to dump LSASS memory |

---

## 📊 MITRE ATT&CK Tactics (Complete List)

MITRE maps the full attack journey:

1. **Reconnaissance** → Gather info
2. **Resource Development** → Create tools
3. **Initial Access** → Enter system
4. **Execution** → Run code
5. **Persistence** → Stay in system
6. **Privilege Escalation** → Gain higher access
7. **Defense Evasion** → Avoid detection
8. **Credential Access** → Steal passwords
9. **Discovery** → Map system
10. **Lateral Movement** → Move across network
11. **Collection** → Gather data
12. **Command & Control** → Communicate
13. **Exfiltration** → Steal data
14. **Impact** → Damage/destruction

---

## ❓ Why MITRE Matters (CRITICAL)

In real cybersecurity jobs:

- ✅ **SOC analysts map alerts to MITRE**
- ✅ Helps **standardize** attack descriptions
- ✅ Helps **detect** attack patterns
- ✅ Helps **understand** attacker behavior
- ✅ Helps **improve** defense strategies

**Real example**:

- Alert: "Suspicious login detected"
- MITRE mapping: Tactic = Credential Access
- Response: Investigate credential compromise

---

## 🔑 Key Terms

| Term | Definition |
| --- | --- |
| **Tactic** | Attacker's goal (WHY) |
| **Technique** | Method used to achieve tactic (HOW) |
| **Procedure** | Real-world implementation of technique |
| **Sub-technique** | Specific variation of technique |

---

## ⚙️ Think Like a SOC Analyst

**Alert comes**: "Suspicious PowerShell execution detected"

**Analysis**:

1. What tactic? → Execution (running code)
2. What technique? → Command Line Interface
3. What procedure? → PowerShell script
4. Action → Investigate and block process

---

## 💡 Exam & Interview Points

**Very common question**: *"What is MITRE ATT&CK?"*

**Best answer**:

> "MITRE ATT&CK is a framework that categorizes attacker behavior into tactics (goals) and techniques (methods). It helps detect, analyze, and respond to cyber threats by mapping real-world attack patterns."
> 

**Additional points**:

- Developed from thousands of real attacks
- Continuously updated
- Used in enterprise security
- Free and publicly available

---

## ⚠️ Common Exam Trap

**Confusion between Tactic and Technique**:

**Wrong**:

- ❌ Treating them as the same thing

**Correct**:

- ✅ **WHY** = Tactic (credential access)
- ✅ **HOW** = Technique (password spraying)

---

## 🚀 Quick Revision

- ▪ **MITRE ATT&CK**: Attack behavior framework
- ▪ **Tactic**: Attacker's goal (WHY)
- ▪ **Technique**: Method used (HOW)
- ▪ **Procedure**: Real implementation
- ▪ **14 tactics**: Cover full attack lifecycle
- ▪ **Used in**: Real SOC jobs and threat analysis
- ▪ **Memory trick**: "WHY → HOW → HOW EXACTLY"