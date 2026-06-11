
---

# Detection Engineering & Threat Simulation Lab

An enterprise-grade detection engineering repository focused on adversary emulation, threat research, and telemetry validation. This portfolio showcases end-to-end detection engineering workflows—from executing atomic attack vectors in a hybrid lab environment to engineering high-fidelity, tuned detection rules within Microsoft Sentinel. This is meant to be a followable repository to learn the end-to-end detection and response engineering process.

---

## 🏗️ Lab Architecture & Data Pipeline

This portfolio is backed by a fully functional, isolated hypervisor and cloud-native security stack. The environment simulates a modern enterprise network to generate authentic endpoint and server telemetry.

```
[Your Local Host PC (VirtualBox)]
   ├── 🖥️ Windows 10 Enterprise Endpoint (Sysmon + Win Security Logs)
   └── 🎛️ Windows Server 2022 Domain Controller (AD + Security Logs)
   └── 🎛️ Ubuntu 22 Linux Server (Syslog Events)
              │
              ▼ [Azure Arc Enabled Infrastructure]
   [Microsoft Azure Log Analytics Workspace]
              │
              ▼ [Data Collection Rules (DCR)]
   [Microsoft Sentinel (SIEM / SOAR Hub)]

```

* **Virtualization:** VirtualBox hosting Windows 10 endpoints and Windows Server 2022 Active Directory infrastructure.
* **Adversary Emulation:** Red Canary's **Atomic Red Team** execution framework.
* **Hybrid Management:** **Azure Arc** agents bridging local virtual infrastructure directly into cloud logging planes.
* **Ingestion Pipeline:** Custom Azure **Data Collection Rules (DCRs)** streaming native Windows Security Event Logs and granular **Sysmon** telemetry.
* **SIEM Platform:** **Microsoft Sentinel** acting as the central analytical workbench for log hunting and KQL rule engineering.

---


## 🛠️ Detection Engineering Workflow

Every detection logged in this portfolio follows a strict, repeatable engineering lifecycle to guarantee high-fidelity alerts and minimize false positives in production environments:

1. **Threat Research & Intelligence:** Reviewing threat intel reports, CISA advisories, or MITRE technical documentation to break down the mechanics of an exploit.
2. **Telemetry Gap Analysis:** Verifying that local logging policies (Sysmon configurations, Advanced Audit Policies) are capturing the necessary telemetry.
3. **Adversary Emulation:** Launching the specific attack technique inside the isolated VM environment using `Invoke-AtomicTest`.
4. **Log Analysis & Query Crafting:** Isolating the attack footprint within Azure Sentinel using Kusto Query Language (KQL) to extract key behavioral indicators.
5. **False Positive Resiliency & Tuning:** Analyzing normal background noise to implement strict exclusion boundaries, ensuring the rule doesn't cause alert fatigue.
6. **Documentation & Version Control:** Committing the rule logic, Sigma schema transformations, and deep-dive technical briefs to this repository.

---

## 🧠 Automation & Emerging Technology Integration

Modern detection engineering requires a force-multiplier approach. This repository integrates automated workflows to assist with alert parsing and operations:

* **Detection-as-Code (DaC):** Rules are tracked cleanly in native KQL formats alongside generic, vendor-agnostic **Sigma** files, allowing seamless deployment to multiple SIEM architectures (Splunk, Elastic, Sentinel).
* **AI-Assisted Alert Triaging (Planned):** Integration scripts utilizing Azure Logic Apps webhooks and LLM APIs to automatically generate human-readable, context-aware triage playbooks when a Sentinel alert fires.

---

## 📂 Repository Navigation Guide

* 📁 **[`/tactics`]**: Contains deep-dive subdirectories for each major threat vector organized by MITRE Tactic. Inside each technique folder, you will find the complete threat analysis markdown, the production-ready `.kql` rule, and tuning notes.
* 📁 **[`/lab-architecture`]**: Contains the granular setup documentation, Sysmon configuration baselines, and Azure Arc onboarding scripts used to construct the environment.
* 📁 **[`/scripts`]**: Central utility directory containing custom automation tools, query parsers, or API connectors used within the lab pipeline.

---

### 📌 Contact 

* **LinkedIn:** (https://www.linkedin.com/in/john-cirello-387311142/)


3. **The Workflow Section:** Proves you don't just write queries; it demonstrates you follow a robust, professional software development lifecycle (SDLC) for security operations.

```
