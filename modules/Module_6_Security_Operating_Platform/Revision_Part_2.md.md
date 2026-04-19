# 📑 Module 6 Part 2 - Revision & Practice

> Cloud Security & Configuration: Complete Part 2 Review
> 

---

## REVISION CHECKLIST

### Topic 6: Cloud Security

- Challenge: Data outside company network
- Problems: No visibility, data leakage, misconfigurations, unauthorized access
- Solution: Cloud security platform

### Topic 7: Prisma

- Palo Alto cloud security platform
- Prisma Access: Secures remote users
- Prisma Cloud: Secures cloud infrastructure
- Benefits: Consistency, visibility, prevention, automation

### Topic 8: Authentication & MFA

- Authentication: Verifies who user is
- SFA: Password only (weak)
- MFA: Password + something (strong)
- MFA factors: Know, Have, Are

### Topic 9: Security Zones & DMZ

- Inside Zone: Internal network (protected)
- Outside Zone: Internet (untrusted)
- DMZ: Middle layer (public servers)
- Purpose: Protect internal network

---

## KEY QUESTIONS

### Q1: Cloud Challenges

What are main cloud security challenges?

Answer: No visibility, data leakage, misconfigurations, unauthorized access

### Q2: Prisma Types

What are the two types of Prisma?

Answer: Prisma Access (users) and Prisma Cloud (infrastructure)

### Q3: Authentication Factors

What are the 3 MFA factors?

Answer: Something you Know (password), Have (phone), Are (biometric)

### Q4: DMZ Purpose

Why does DMZ exist?

Answer: To separate public servers from internal network and protect critical assets

### Q5: Zero Trust in Zones

Does Zero Trust apply within DMZ?

Answer: Yes, even DMZ is not automatically trusted - continuous verification needed

---

## COMPARISON TABLES

### SFA vs MFA

| Factor | SFA | MFA |
| --- | --- | --- |
| Methods | Password | 2+ methods |
| Security | Weak | Strong |
| Theft Risk | High | Low |
| Recommendation | Avoid | Use Always |

### Zone Security Rules

| Direction | Rule | Why |
| --- | --- | --- |
| Inside -> Outside | Allowed | Employees browse |
| Outside -> Inside | Blocked | Hackers blocked |
| Outside -> DMZ | Limited | Only needed access |
| DMZ -> Inside | Blocked | Isolation |

### Prisma Types

| Type | Purpose | Protects |
| --- | --- | --- |
| Access | Secure users | Remote employees |
| Cloud | Secure infrastructure | AWS, Azure, GCP |

---

## MEMORY TRICKS

"Cloud = No boundary -> Security everywhere"

"Prisma = Access (users) + Cloud (infrastructure)"

"Two factors = Twice as secure"

"DMZ = Buffer Zone = Protection"

"Internet -> DMZ -> Internal (layered defense)"

---

## PRACTICE QUESTIONS

### Q1: Cloud Security

Why is cloud security important?

A) Only for large companies

B) Data is outside company control

C) Optional feature

D) Only for developers

Answer: B

### Q2: Prisma

Prisma Access protects:

A) Cloud infrastructure

B) Only office users

C) Remote users anywhere

D) Only web servers

Answer: C

### Q3: MFA

Which is strongest authentication?

A) Password only

B) Password + hint

C) Password + OTP

D) Username + password

Answer: C

### Q4: DMZ

What separates DMZ from internal network?

A) Nothing

B) Another firewall

C) Encryption

D) Distance

Answer: B

### Q5: Zone Rules

Can DMZ directly access internal network?

A) Yes, always

B) Only with VPN

C) No, blocked

D) Only for admins

Answer: C

---

## QUICK EXAM SUMMARY

Cloud security is critical in modern orgs

Prisma = Palo Alto cloud solution

MFA is non-negotiable for security

DMZ protects internal network

Zero Trust applies everywhere

Layered defense = best security

---

MODULE 6 COMPLETE!