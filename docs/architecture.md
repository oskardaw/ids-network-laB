# Lab Architecture

## Overview

The environment was designed to compare the behavior of three intrusion detection and network monitoring systems: Snort, Suricata, and Zeek.

The setup was fully isolated and operated in a controlled local network to ensure reproducibility and eliminate external traffic influence.

## System Architecture

The lab consisted of three virtual machines:

### Attacker Machine
- OS: Kali Linux
- Role: Traffic generation (ICMP, TCP, UDP)
- Tools: ping, /dev/tcp, /dev/udp, manual traffic generation

### Target Machine (Victim)
- OS: Ubuntu
- Role: Service endpoint receiving network traffic

### Monitoring Machine (IDS Sensor)
- OS: Ubuntu
- Role: Passive network traffic analysis
- Tools:
  - Snort
  - Suricata
  - Zeek

## Network Configuration

- All machines were located in the same private subnet
- Static IP addressing was used
- Network interface: ens33
- Monitoring mode: passive (no packet injection or blocking)

## Key Design Principle

The IDS systems operated without influencing network traffic to ensure that all observed behavior reflected real packet flow.
