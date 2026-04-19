# 📑 Module 3 Part 2 — Revision & Practice

> Exploitation Techniques and Advanced Threat Detection
> 

---

## ✅ Revision Checklist

### Topic 5: Vulnerabilities & Exploits

- [ ]  Vulnerability = weakness
- [ ]  Exploit = attack method
- [ ]  Zero-day = unknown vulnerability
- [ ]  Patch = fix by vendor
- [ ]  Timeline: exist → discover → exploit → disclose → patch
- [ ]  Most attacks use exploits

### Topic 6: Business Email Compromise (BEC)

- [ ]  BEC = email fraud
- [ ]  No malware sometimes
- [ ]  Types: phishing, spear-phishing, whaling, pharming
- [ ]  Social engineering attack
- [ ]  $2.9 billion annual losses
- [ ]  Employee training = best defense

### Topic 7: Bots & Botnets

- [ ]  Bot = infected device
- [ ]  Botnet = network of bots
- [ ]  C2 = Command & Control server
- [ ]  Types: spam, DDoS, financial, mining
- [ ]  Scale makes dangerous
- [ ]  Break C2 connection to stop

### Topic 8: WildFire (Advanced Detection)

- [ ]  Cloud-based malware detection
- [ ]  Detects unknown threats
- [ ]  Analysis techniques: dynamic, static, ML, bare metal, recursive
- [ ]  Better than traditional AV
- [ ]  Shares protection globally
- [ ]  Essential for zero-day defense

---

## ❓ Key Questions to Answer

1. **Difference: Vulnerability vs Exploit?**
    - Vulnerability = weakness; Exploit = code to trigger it
2. **Why is BEC effective?**
    - Targets human behavior; no malware needed
3. **How to stop botnet?**
    - Break C2 connection
4. **How does WildFire detect unknown malware?**
    - Multiple analysis: dynamic, static, ML, etc.
5. **Why is zero-day most dangerous?**
    - No patch available; no defense possible

---

## 📊 Comparison Tables

### Vulnerability Timeline

| Phase | Status | Risk Level | Defense |
| --- | --- | --- | --- |
| Exists | Unknown | None | N/A |
| Discovered | Known by attacker | Extreme | None |
| Disclosed | Public | High | Patch |
| Patched | Fixed | Low | Update |

### Attack Types Comparison

| Attack | Type | Malware? | Detection |
| --- | --- | --- | --- |
| Vuln/Exploit | Technical | Maybe | Pattern |
| BEC | Social | No | Verification |
| Botnet | Technical | Yes | C2 blocking |
| Zero-Day | Technical | Maybe | Behavior |

### Analysis Methods

| Method | What | Detects | Limitation |
| --- | --- | --- | --- |
| Dynamic | Behavior | Runtime actions | VM evasion |
| Static | Code | Signatures | Unknown |
| ML | Patterns | Novel threats | False positive |
| Bare Metal | Real HW | Evasion | Slow |
| Recursive | Multi-stage | Complex | Resource |

---

## 🧠 Memory Tricks

### "Weakness → Exploit → Attack"

**Vulnerability exploitation cycle**

### "Fake Email → Trust → Money Lost"

**BEC attack flow**

### "Many Bots = Massive Attack"

**Botnet power**

### "Analyze → Detect → Share → Protect"

**WildFire process**

---

## 📝 Practice Questions

### Q1: Vulnerability Types

**Zero-day is dangerous because:**

A) It spreads fast

B) No patch available

C) Uses multiple files

D) Requires admin

✅ **Answer: B**

### Q2: BEC Prevention

**Best defense against BEC?**

A) Better firewall

B) Malware detection

C) Employee verification

D) Email encryption

✅ **Answer: C**

### Q3: Botnet Control

**To stop botnet:**

A) Kill bots one by one

B) Patch all systems

C) Break C2 connection

D) Block all traffic

✅ **Answer: C**

### Q4: WildFire

**WildFire advantage over AV:**

A) Faster

B) Cheaper

C) Detects unknown threats

D) No false positives

✅ **Answer: C**

---

## 🎯 Advanced Questions

### Q5: Zero-Day Exploitation

**Why attacker doesn't publish zero-day immediately?**

A) Wants to use it first

B) Sells it on dark web

C) Profits from exploitation

D) All of above

✅ **Answer: D** - Multiple revenue streams

### Q6: BEC vs Malware

**Key difference?**

A) BEC uses malware

B) BEC is social engineering

C) Malware always better

D) No difference

✅ **Answer: B**

---

## 🐟 Quick Summary for Exam

**Part 2 Essentials:**

- ✔ Vulnerability = weakness
- ✔ Exploit = attack method
- ✔ BEC = email fraud
- ✔ Botnet = amplified attack
- ✔ Zero-day = impossible to defend
- ✔ WildFire = advanced detection

---

## 📚 Real-World Scenarios

### Scenario 1: Zero-Day

**Situation**: New vulnerability found in Windows

**Stage**: Before patch

**Risk**: Extreme - no defense

**Action**: No patch, monitor only

### Scenario 2: BEC Attack

**Situation**: CEO lookalike email to finance

**Risk**: High - works on humans

**Defense**: Call CEO to verify

**Cost**: Prevents $500K+ loss

### Scenario 3: Botnet DDoS

**Situation**: Website under attack

**Cause**: 1M compromised devices

**Defense**: Block C2 servers

**Result**: Attack stops

---

**Module 3 Complete! You've mastered malware, exploitation, and detection!** 🌟📚