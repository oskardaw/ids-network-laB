# IDS Home Network Analysis Lab

## Overview

This project presents a laboratory-based comparative analysis of three network intrusion detection and monitoring systems: **Snort, Suricata, and Zeek**.

The goal of the project is to evaluate and compare how each system behaves under identical network conditions in a controlled virtualized environment, simulating a small home network.

The analysis focuses on detection capability, logging approaches, and behavioral visibility of each tool when processing various types of network traffic and simulated attack scenarios.

---

## Objective

The main objective of this project is to:

- Compare signature-based and behavior-based detection approaches
- Analyze IDS/NSM system behavior under controlled attack scenarios
- Evaluate differences in alert generation, logging detail, and usability
- Understand strengths and limitations of each tool in a home network context

---

## Lab Architecture

The environment consists of three virtual machines connected in an isolated subnet:

- **Attacker (Kali Linux)** – generates network traffic and simulates attacks
- **Victim (Ubuntu Server)** – target system receiving traffic
- **IDS Sensor (Ubuntu Server)** – runs Snort, Suricata, and Zeek (individually)

All systems operate in a passive monitoring setup where the IDS sensor observes traffic without interfering with network communication.

---

## Tools and Technologies

- Snort
- Suricata
- Zeek
- Kali Linux
- Ubuntu Server
- VirtualBox / VMware (virtualization environment)
- TCP/IP networking tools (ping, /dev/tcp, /dev/udp)

---

## Methodology

Each IDS tool was tested independently under identical conditions to ensure result consistency.

Test scenarios included:

- ICMP echo requests
- TCP connection attempts
- UDP traffic generation
- Port scanning simulation
- Flood-style traffic generation

Traffic was manually generated from the attacker machine using native Linux tools to maintain full control over test conditions.

Data was collected in the form of:

- IDS alerts (Snort, Suricata)
- Network event logs (Zeek: conn.log, icmp.log)
- Traffic generation logs
- Screenshots of execution results

---

## Key Findings

- Snort provides fast, rule-based detection but limited context awareness
- Suricata offers richer and more detailed alert output compared to Snort
- Zeek provides the deepest visibility into network behavior but requires manual log analysis
- Signature-based systems are effective for known attack patterns but depend heavily on rule quality
- Behavior-based analysis (Zeek) is better suited for forensic and investigative workflows
- Combining both approaches provides the most complete security visibility

---

## Results Summary

- IDS systems react differently to identical traffic depending on detection model
- High traffic scenarios increase noise and false positives in signature-based systems
- Zeek provides the best analytical depth but requires more expertise for interpretation
- Proper rule tuning significantly improves detection accuracy

---

## Project Structure

docs/
architecture.md
methodology.md
findings.md
architecture_diagram.md

analysis/
(results and interpretation)

configs/
(IDS configurations if available)

logs/
sample logs and outputs


---

## Conclusion

This project demonstrates practical differences between three widely used network security monitoring systems.

The results show that no single tool provides complete coverage. Instead, a layered approach combining signature-based detection (Snort, Suricata) with behavioral analysis (Zeek) offers the most effective monitoring strategy in a network security environment.

---

## Note

This repository is based on an engineering thesis project and represents a reconstructed and adapted version of the original laboratory environment for portfolio purposes.
