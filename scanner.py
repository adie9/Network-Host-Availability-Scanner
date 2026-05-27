import csv
from pathlib import Path
from pythonping import ping

HOSTS = "data/hosts.txt"
OUTPUT = "output/scan_results.csv"


def load_hosts(file_path: str) -> list[str]:
    """
    Checks if file exists. Proceeds normally if so.

    Loads a list of host IP addresses from a text file.

    Each non-empty line in the file is treated as a host entry.
    Whitespace is stripped automatically.
    """

    file_path = Path(file_path)
    if not file_path.exists():
        print("File not found")
        return []

    with open(file_path, "r") as f:
        hosts = []
        for line in f:
            line = line.strip()  # Remove whitespace
            if line:  # Skip empty lines
                hosts.append(line)
    return hosts


def ping_host(ip: str) -> dict:
    """
    Ping a single IP address using pythonping.

    Sends one ICMP echo request and returns structured data
    describing the host's status and latency.
    """
    response = ping(ip, count=1)
    if response.success():
        latency = response.rtt_avg_ms
        return {"ip": ip, "status": "UP", "latency": latency}
    else:
        return {"ip": ip, "status": "DOWN", "latency": -1}


def scan_hosts(host_list: list[str]) -> list[dict]:
    """
    Pings all hosts in the provided list and collects the results.
    """
    results = []
    for ip in host_list:
        result = ping_host(ip)  # Ping each host individually
        results.append(result)
    return results


def save_results_to_csv(results: list[dict], output_path: str) -> None:
    """
    Save scan results to a csv file.

    The csv file will contain the columns: ip, status, latency_ms
    """
    with open(output_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ip", "status", "latency_ms"])  # Header row
        for result in results:
            writer.writerow([result["ip"], result["status"], result["latency"]])


def main() -> None:
    hosts = load_hosts(HOSTS)
    if not hosts:
        print("No hosts to scan. Exiting...")
        return
    scan_results = scan_hosts(hosts)
    save_results_to_csv(scan_results, OUTPUT)


if __name__ == "__main__":
    main()
