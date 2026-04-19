# Topic 10: Access Control Models (BLP, Biba, Clark-Wilson, Chinese Wall)

> Models Protecting Confidentiality and Integrity
> 

---

## 📖 SIMPLE EXPLANATION

**These models define how access is controlled for confidentiality and integrity**

Multiple models for different purposes

---

## 🔴 1. BELL-LA PADULA (BLP) MODEL

### Focus: **Confidentiality (data secrecy)**

### Rules:

❌ No Read Up

❌ No Write Down

### Example:

Employee (Confidential) cannot read Secret data

### Memory Trick:

**"Read Down, Write Up"**

---

## 🔵 2. BIBA MODEL

### Focus: **Integrity (data correctness)**

### Rules:

❌ No Read Down

❌ No Write Up

### Opposite of BLP

High-level system cannot read low-trust data

### Memory Trick:

**"Integrity flows downward"**

---

## 🔶 3. LOW-WATERMARK MODEL

### Extension of Biba

- Allows read down
- But reduces user integrity

User integrity lowered after reading low-level data

---

## 🔷 4. CLARK-WILSON MODEL

### Focus: **Data integrity in transactions**

- Uses rules
- Uses verification

Example: Bank transaction system ensures balance

---

## 🔺 5. CHINESE WALL MODEL

### Focus: **Prevents conflict of interest**

- User cannot access competing data
- Prevents cross-access

Example: Consultant cannot work for two competitors

---

## 📊 MODELS COMPARISON

| Model | Focus | Key Rule |
| --- | --- | --- |
| **BLP** | Confidentiality | No Read Up |
| **Biba** | Integrity | No Read Down |
| **Clark-Wilson** | Integrity | Transaction control |
| **Chinese Wall** | Conflict | No cross-access |

---

## ⚠️ EXAM TRAP

### ❌ BLP vs Biba confusion

### ✅ Remember:

- **BLP** → secrecy
- **Biba** → correctness

---

## 🧠 MASTER MEMORY TRICK

### "BLP = Secret, Biba = Safe data"

---

## 🧠 QUICK SUMMARY

✔ **BLP** → confidentiality

✔ **Biba** → integrity

✔ **Clark-Wilson** → transactions

✔ **Chinese Wall** → conflict prevention

---

**Module 4 Part 2 Topics Complete! Ready for Revision Page?** 📚