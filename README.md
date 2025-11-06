# 🧠 Network Intrusion Detection System (Snort IDS Lab)

[![Made with Snort](https://img.shields.io/badge/IDS-Snort%202.9.20-blue)](#)
[![Python](https://img.shields.io/badge/Python-3.x-informational)](#)
[![Status](https://img.shields.io/badge/Status-Working%20Demo-success)](#)
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](#)

A reproducible **Network Intrusion Detection** mini-lab built on **Snort 2.x** (Ubuntu/Parallels).  
It detects **SSH brute force** and **port scans** using **custom rules** and simulated traffic from **Python/Scapy** and **hping3**.

---

## ✨ Features
- **Custom Snort rules** with unique SIDs and `detection_filter` thresholds  
- **Inbound** and **outbound** scan detection  
- Run on **loopback (lo)** (self-traffic) or **NIC (enp0s5)** (network)  
- **Traffic generators:** `generate_scan.py`, `generate_ssh_bruteforce.py` (+ hping3 fallback)  
- **Alert parser:** convert `alert` (fast) into CSV for analysis  
- **One-page portfolio PDF** with screenshots and results

---

## 🧩 Architecture (mini lab)
┌───────────────┐     SYN/UDP test traffic      ┌───────────────┐
│ Traffic Gen   │ ─────────────────────────────> │  Snort 2.x    │
│ (Scapy/hping) │                                │ (lo / enp0s5) │
└───────────────┘                                └───────────────┘
│                                              │
└──────────────>  alert.fast / console  <──────┘

---

.
├── snort/
│   ├── local.rules              # Custom rules (unique SIDs)
│   └── snort.conf.sample        # Snippet (include + HOME_NET + fast output)
├── setup_scripts/
│   ├── run_snort_enp0s5.sh      # Run on NIC (console alerts)
│   └── run_snort_lo.sh          # Run on loopback (console alerts)
├── traffic/
│   ├── generate_scan.py         # Benign SYN scan generator
│   └── generate_ssh_bruteforce.py
├── utils/
│   └── parse_alert_fast.py      # Convert alert to CSV
├── analysis/cheatsheet.md
├── sample_data/Network_IDS_Report_TEMPLATE.md
├── Snort_Project_Portfolio.pdf  # One-page PDF with screenshots/results
└── assets/                      # (Optional) screenshots for README


### 🧪 Example Rules (snippet)
# Inbound SSH brute force (external -> HOME_NET)
alert tcp any any -> $HOME_NET 22 (msg:"LOCAL SSH brute force test (inbound)";
    flags:S; flow:stateless; detection_filter:track by_src, count 3, seconds 10;
    sid:5000001; rev:1;)

# Outbound port scan (HOME_NET -> any)
alert tcp $HOME_NET any -> any any (msg:"LOCAL Port scan test (outbound)";
    flags:S; flow:stateless; detection_filter:track by_src, count 5, seconds 10;
    sid:5000002; rev:1;)

    🧰 Tech

Snort 2.9.x, Python 3.x, Scapy, hping3, Ubuntu (Parallels VM)

👤 Author

Mahmudur Rahman
Cybersecurity | SOC Analyst Track | CompTIA Security+
LinkedIn: https://www.linkedin.com/in/mahmudurrahmanmikat/
