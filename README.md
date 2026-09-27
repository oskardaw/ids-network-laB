# Comparative Analysis of Intrusion Detection Systems (IDS)

A controlled home network laboratory designed to evaluate, test, and compare the performance, detection coverage, and log generation capabilities of **Snort**, **Suricata**, and **Zeek** under simulated network attack scenarios.

## Project Scope & Objectives

- Deploy and configure Snort, Suricata, and Zeek in a segmented lab environment.
- Generate controlled network traffic and simulate common attack vectors (port scans, brute-force attacks, web exploits).
- Compare rule-matching performance, signature detection efficiency, and protocol analysis metadata.

## Environment Architecture

- **Traffic Generator / Attacker**: Kali Linux (Nmap, Metasploit, Scapy)
- **Monitoring Layer**: 
  - **Snort 3**: Signature-based detection and packet inspection.
  - **Suricata**: Multi-threaded threat detection and EVE JSON logging.
  - **Zeek (Bro)**: Behavioral network analysis and protocol logging.
- **Target Network**: Vulnerable Linux endpoints in a isolated subnet.

## Comparative Matrix

| Feature / Engine | Snort | Suricata | Zeek |
| :--- | :--- | :--- | :--- |
| **Primary Focus** | Signature Detection | Multi-threaded Signature/Anomaly | Network Analysis & Protocol Metadata |
| **Performance** | Single/Multi-threaded | High Performance (Multi-threaded) | Event-driven Data Collection |
| **Output Format** | Unified2 / Text Logs | EVE JSON | Structured Tab-Separated / JSON Logs |
| **Best Use Case** | Inline Prevention (IPS) | Enterprise Intrusion Detection | Network Forensics & Threat Hunting |

## Tested Scenarios & Rule Triggers

1. **Reconnaissance**: Nmap SYN Scans & Service Enumeration (`TCP SYN flood` detection).
2. **Web Exploitation**: Directory Bruteforcing (`Gobuster` requests) & Command Injection triggers.
3. **Malicious Traffic**: Custom PCAP replay testing rule accuracy across all three engines.

## Key Findings & Conclusion

- **Snort** excels at quick, signature-based blocking at the perimeter with low syntax overhead.
- **Suricata** provides superior multi-core CPU utilization and rich, easy-to-parse JSON output for SIEM integration.
- **Zeek** provides unmatched visibility for post-incident investigation, offering rich session-level metadata rather than simple alerts.
