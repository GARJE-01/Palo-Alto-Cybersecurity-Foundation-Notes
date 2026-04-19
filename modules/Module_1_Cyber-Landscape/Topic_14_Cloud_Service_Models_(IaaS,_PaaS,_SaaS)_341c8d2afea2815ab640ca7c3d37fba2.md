# Topic 14: Cloud Service Models (IaaS, PaaS, SaaS)

## 📌 Definition

Three distinct models defining responsibility for security and management.

---

## ⚙️ How It Works (Control & Responsibility)

| Model | Provider Controls | User Controls | Example |
| --- | --- | --- | --- |
| **IaaS** | Network, Storage, Servers | OS, Middleware, Apps | AWS EC2, DigitalOcean |
| **PaaS** | Network, Storage, Servers, OS | Middleware, Apps | Heroku, Google App Engine |
| **SaaS** | Everything | User account settings | Gmail, Slack, Office 365 |

---

## 🌍 Real-World Example

- **IaaS** → Rent virtual server, you install everything
- **PaaS** → Deploy app, platform handles OS + runtime
- **SaaS** → Just use Gmail, no installation needed

---

## ❓ Why It Matters

**Defines security responsibility** — crucial for determining who fixes what.

---

## 🔑 Key Terms

| Term | Definition |
| --- | --- |
| **IaaS** | Infrastructure as a Service |
| **PaaS** | Platform as a Service |
| **SaaS** | Software as a Service |
| **Shared Responsibility Model** | Provider and customer split security duties |

---

## 💡 Exam & Interview Points

- **VERY IMPORTANT: "Difference between IaaS, PaaS, SaaS?" (Asked frequently)**
- Key insight: Control ↓ from IaaS to SaaS, Responsibility ↓ from user to provider
- Interview focus: Who is responsible for what in each model

---

## 🚀 Quick Revision

- ▪ IaaS = Most user control, most responsibility
- ▪ PaaS = Shared control and responsibility
- ▪ SaaS = Least user control, provider manages most
- ▪ Security responsibility differs by model