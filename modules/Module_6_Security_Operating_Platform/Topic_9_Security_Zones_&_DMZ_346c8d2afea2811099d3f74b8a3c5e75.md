# Topic 9: Security Zones & DMZ

> Network divided into protected sections
> 

---

## SIMPLE EXPLANATION

**Security Zones** = Network divided into sections

### Types of Zones:

1. Inside Zone (internal network)
2. Outside Zone (internet)
3. DMZ (middle layer)

---

## ZONE ARCHITECTURE

```
Internet -> Firewall -> DMZ -> Firewall -> Internal Network
```

### Inside Zone:

- Internal company network
- Highly protected
- Employee computers, databases, apps

### Outside Zone:

- The public internet
- Untrusted, Dangerous

### DMZ (Demilitarized Zone):

- Middle layer
- Semi-trusted
- Public servers (web, email, DNS)

---

## WHY DMZ EXISTS

**"Expose public services, protect internal network"**

### Problems DMZ Solves:

1. Malware from internet stops at DMZ
2. Hacking attempts contained in DMZ
3. Limited access to sensitive data

---

## SECURITY RULES

Inside -> Outside: Generally allowed

Outside -> Inside: Generally blocked

Outside -> DMZ: Limited allowed

DMZ -> Inside: Mostly blocked

---

## REAL-WORLD EXAMPLE

**Employee accesses web server:**

1. Employee (inside) requests website
2. Traffic passes through firewall
3. Reaches DMZ web server
4. Data returned to employee

**Hacker tries to attack:**

1. Hacker (outside) attacks web server
2. Firewall blocks attack
3. Internal network safe!

---

## EXAM TRAP

**WRONG:**

- "DMZ is fully trusted"

**RIGHT:**

- "DMZ is semi-trusted and isolated from internal network"

---

## MEMORY TRICK

**"DMZ = Buffer Zone = Protection"**

---

## QUICK SUMMARY

Inside = internal network (protected)

Outside = internet (untrusted)

DMZ = middle layer (public servers)

DMZ protects internal network

Multiple firewalls provide defense