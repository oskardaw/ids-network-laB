import re
from collections import defaultdict

LOG_FILE = "auth.log"

pattern = re.compile(r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)")

def parse_logs(file_path):
    ip_counts = defaultdict(int)

    try:
        with open(file_path, "r") as file:
            for line in file:
                match = pattern.search(line)
                if match:
                    ip = match.group(1)
                    ip_counts[ip] += 1
    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")
        return {}

    return ip_counts

def print_report(ip_counts, threshold=3):
    print("\n=== SSH Brute-force Analysis Report ===\n")

    suspicious = {ip: count for ip, count in ip_counts.items() if count >= threshold}

    if not suspicious:
        print("No suspicious activity detected.")
        return

    print("Potential brute-force attempts detected:\n")

    for ip, count in sorted(suspicious.items(), key=lambda x: x[1], reverse=True):
        print(f"IP: {ip} | Failed attempts: {count}")

    print("\n=== End of Report ===")

if __name__ == "__main__":
    ip_counts = parse_logs(LOG_FILE)
    print_report(ip_counts)
