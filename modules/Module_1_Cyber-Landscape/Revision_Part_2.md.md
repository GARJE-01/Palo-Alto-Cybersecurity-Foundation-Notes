# 📑 Module 1 Part 2 — Revision & Practice

> Cloud Security, SaaS Risks, and Compliance Review
> 

---

## ✅ Revision Checklist

Before the exam, ensure you understand:

### Topic 11: Modern Computing Trends

- [ ]  What are the latest computing trends (IoT, Edge, etc.)?
- [ ]  How do these trends impact security?
- [ ]  Know examples of modern computing environments

### Topic 12: BYOD & Consumerization

- [ ]  What is BYOD and why is it risky?
- [ ]  Difference between corporate devices and personal devices
- [ ]  Security challenges of BYOD
- [ ]  MDM (Mobile Device Management) basics

### Topic 13: Cloud Computing Basics

- [ ]  What is cloud computing?
- [ ]  Advantages and disadvantages
- [ ]  Types: Public, Private, Hybrid, Community clouds
- [ ]  Key characteristics of cloud (On-demand, Elasticity, etc.)

### Topic 14: Cloud Service Models

- [ ]  IaaS: What is managed vs. customer responsibility?
- [ ]  PaaS: What is managed vs. customer responsibility?
- [ ]  SaaS: What is managed vs. customer responsibility?
- [ ]  Shared responsibility model in detail
- [ ]  Which model requires most security effort?

### Topic 15: Cloud Security Challenges

- [ ]  Top cloud security risks
- [ ]  Data exposure risks in cloud
- [ ]  Misconfiguration issues
- [ ]  Insider threats in cloud
- [ ]  Compliance challenges

### Topic 16: Zero Trust in Cloud

- [ ]  What is Zero Trust model?
- [ ]  "Never trust, always verify" principle
- [ ]  How Zero Trust applies to cloud
- [ ]  Benefits of Zero Trust
- [ ]  Implementation considerations

### Topic 17: SaaS Application Risks

- [ ]  What is SaaS and its risks?
- [ ]  Shadow IT problem
- [ ]  Unsanctioned cloud apps
- [ ]  Data leakage through SaaS
- [ ]  Account takeover risks

### Topic 18: Types of SaaS Data Exposure

- [ ]  Data exfiltration methods
- [ ]  Misconfigured sharing settings
- [ ]  Insecure integrations
- [ ]  Credential theft
- [ ]  Real-world SaaS breach examples

### Topic 19: SaaS Security Best Practices

- [ ]  Employee training and awareness
- [ ]  SaaS governance framework
- [ ]  Cloud Access Security Brokers (CASB)
- [ ]  Activity monitoring
- [ ]  Data Loss Prevention (DLP)
- [ ]  API security

### Topic 20: Compliance vs. Security

- [ ]  What is the difference?
- [ ]  Can you be compliant but not secure?
- [ ]  Can you be secure but not compliant?
- [ ]  Risk-based approach
- [ ]  Business impact assessment

### Topic 21: Important Regulations

- [ ]  **GDPR**: What it covers, who it applies to, key requirements
- [ ]  **HIPAA**: Healthcare data protection, who must comply
- [ ]  **PCI DSS**: Payment card security, 12 main requirements
- [ ]  **CCPA**: California privacy law, user rights
- [ ]  **SOC 2**: Security, Availability, Processing Integrity, Confidentiality, Privacy
- [ ]  How regulations impact cloud adoption

---

## ❓ Practice Questions

### Question 1: IaaS vs PaaS vs SaaS

A company wants to move from on-premises to cloud. Which service model shifts the most responsibility to the vendor?

**Answer**: SaaS shifts the most responsibility to the vendor

### Question 2: Zero Trust

Which principle is central to Zero Trust architecture?

**Answer**: "Never trust, always verify" - authentication/authorization for every access

### Question 3: Compliance

Can a company be compliant with regulations but still have security vulnerabilities?

**Answer**: Yes - compliance checks specific requirements; security is broader

### Question 4: GDPR

Which regulation provides users the "right to be forgotten"?

**Answer**: GDPR (General Data Protection Regulation)

### Question 5: SaaS Risks

What is the biggest security risk when employees use unsanctioned cloud apps?

**Answer**: Shadow IT - IT doesn't know about it, can't protect it

---

## 📊 Comparison Tables

### Cloud Service Models

| Responsibility | IaaS | PaaS | SaaS |
| --- | --- | --- | --- |
| Infrastructure | Vendor | Vendor | Vendor |
| Platform | Customer | Vendor | Vendor |
| Applications | Customer | Customer | Vendor |
| Data | Customer | Customer | Customer |
| Users | Customer | Customer | Customer |
| Devices | Customer | Customer | Customer |

### Key Regulations

| Regulation | Scope | Key Requirement | Applies To |
| --- | --- | --- | --- |
| **GDPR** | Data privacy (EU) | Right to be forgotten | All orgs handling EU data |
| **HIPAA** | Healthcare data | Encryption + audit logs | Healthcare providers |
| **PCI DSS** | Payment cards | 12 main controls | Payment processors |
| **CCPA** | Consumer privacy (CA) | Opt-out rights | CA residents' data |

---

## 🎯 Key Takeaways for Part 2

1. **Cloud Models**: IaaS → PaaS → SaaS (responsibility increases on vendor)
2. **Zero Trust**: Standard for modern cloud security
3. **SaaS Risks**: Shadow IT is the biggest challenge
4. **Compliance**: GDPR, HIPAA, PCI DSS are most important
5. **Shared Responsibility**: Customer must understand their role
6. **Data is Customer Responsibility**: In all cloud models, data protection is customer's job
7. **Cloud Security Layers**: Multiple controls needed (IAM, encryption, monitoring)

---

## 📚 Topics to Review Before Exam

- [ ]  Summarize the shared responsibility model for each service type
- [ ]  List 5 BYOD security risks
- [ ]  Explain how Zero Trust differs from traditional perimeter security
- [ ]  Compare GDPR and CCPA in terms of user rights
- [ ]  Describe the Shadow IT problem and solutions
- [ ]  Explain why SaaS requires different security approach
- [ ]  List 3 common SaaS misconfigurations
- [ ]  Understand the business impact of cloud security breaches

---

## 💡 Interview Tips

✅ **Common Questions**:

- "Explain the shared responsibility model" - Know this inside out!
- "What are the risks of cloud adoption?" - Data exposure, compliance, insider threats
- "How would you secure a SaaS environment?" - CASB, DLP, activity monitoring
- "What is Zero Trust?" - "Never trust, always verify"
- "What's the difference between GDPR and CCPA?" - Geographic scope, user rights

✅ **Practice saying**: 

- "In the cloud, the vendor manages X, but WE manage data security"
- "Shadow IT is a bigger problem than sanctioned cloud apps"
- "Compliance is not the same as security"
- "Zero Trust means no implicit trust based on network location"

---

## 🔗 Connection to Real World

**Scenario**: Your company is moving to Microsoft 365 (SaaS)

**Security Questions**:

1. Who owns the security of the 365 infrastructure? → Microsoft
2. Who owns the security of your company data? → You
3. What if an employee leaves - who deletes the data? → You
4. What if Microsoft is breached? → Your data might be exposed (you still own it)
5. What about GDPR compliance? → You're responsible for enforcement

---

**Ready for the exam? Review this checklist one more time!** 📋