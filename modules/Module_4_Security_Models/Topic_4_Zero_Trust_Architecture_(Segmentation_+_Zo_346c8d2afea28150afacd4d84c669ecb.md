# Topic 4: Zero Trust Architecture (Segmentation + Zones)

> Segmentation, Trust Zones, and Implementation
> 

---

## 📖 SIMPLE EXPLANATION

**Zero Trust is implemented using:**

- Segmentation
- Trust Zones
- Segmentation Platform (Firewall)

👉 Network divided into small secure zones

👉 Each zone has its own rules

👉 Zones are isolated from each other

---

## 🔴 1. SEGMENTATION (Micro-Perimeter)

### Definition:

Network divided into smaller parts

### Real-World Example:

- **HR data zone** (separate)
- **Finance data zone** (separate)
- **Web application zone** (separate)

👉 If attacker enters HR → cannot access Finance

---

## 🔵 2. TRUST ZONES

### Definition:

Group of resources with same trust level

### Example Zones:

1. **User Zone**: Employee computers
2. **Guest WiFi Zone**: Visitors
3. **Database Zone**: Sensitive data
4. **Web App Zone**: Public applications

---

## 🔶 3. SEGMENTATION PLATFORM (Firewall)

### Definition:

Controls communication between zones

### What It Does:

- Allows only permitted traffic
- Blocks everything else
- Monitors activity

---

## ⚠️ VERY IMPORTANT RULE

**Even inside same zone:**

Traffic is NOT trusted automatically

👉 All communication still inspected

👉 All traffic still logged

👉 Policies still enforced

---

## ⚠️ EXAM TRAP

### ❌ Wrong:

"Zone = trusted area"

### ✅ Right:

"Zone = controlled area (still monitored)"

---

## 🧠 MEMORY TRICK

### "Divide → Control → Monitor"

---

## 🧠 QUICK SUMMARY

✔ Network divided into zones

✔ Firewall controls access

✔ Micro-perimeter protects data

✔ No implicit trust anywhere

---

**Ready for Topic 5: Advantages of Zero Trust?** 📚