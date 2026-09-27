# Log Analyzer Script

## Description

This script analyzes Linux authentication logs (`auth.log`) to detect potential SSH brute-force attempts.

It extracts failed login attempts, groups them by IP address, and identifies suspicious activity based on a configurable threshold.

---

## Features

- Parsing SSH authentication logs
- Detection of failed login attempts
- IP-based aggregation
- Simple brute-force detection logic

---

## Usage

Run the script:

```bash
python3 log_analyzer.py

