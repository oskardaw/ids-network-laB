# Methodology

## Objective

The goal was to compare the effectiveness of Snort, Suricata, and Zeek in detecting and analyzing network attacks in a controlled environment.

## Test Design

Each IDS was tested independently to avoid interference between systems. Only one monitoring tool was active at a time.

All tests were executed under identical network conditions to ensure comparability of results.

## Traffic Generation

Traffic was generated manually from the attacker machine (Kali Linux) using native system tools:

- ICMP traffic: `ping`
- TCP connections: `/dev/tcp`
- UDP traffic: `/dev/udp`
- Port scanning and flood simulation

No external penetration testing frameworks were used in order to maintain full control over generated traffic.

## Test Scenarios

The following scenarios were executed:

- ICMP echo requests
- TCP SYN connection attempts
- UDP packet transmission
- Port scanning simulation
- Flood-style traffic generation

## Data Collection

For each test case, the following data was collected:

- Packet generation logs (attacker side)
- IDS alerts (Snort, Suricata)
- Network event logs (Zeek: conn.log, icmp.log)
- Screenshots documenting execution results

## Zeek Analysis Approach

Unlike Snort and Suricata, Zeek was evaluated through event logs rather than alerts. Analysis focused on:

- connection patterns
- traffic anomalies
- scanning behavior detection

## Output Usage

Collected data was later used to compare:

- detection accuracy
- verbosity of logs
- false positive tendency
- usability of each system
