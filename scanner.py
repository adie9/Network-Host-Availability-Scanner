from pythonping import ping

HOSTS = "data/hosts.txt"
OUTPUT = "output.txt"


def load_hosts(file_path):
    with open(file_path, "r") as f:
        hosts = []
        for line in f:
            line = line.strip()
            if line:
                hosts.append(line)
    return hosts


def ping_host(ip):
    response = ping(ip, count=1)
    if response.success():
        latency = response.rtt_avg_ms
        return {"ip": ip, "status": "UP", "latency": latency}
    else:
        return {"ip": ip, "status": "DOWN", "latency": -1}


def scan_hosts(host_list):
    results = []
    for ip in host_list:
        result = ping_host(ip)
        results.append(result)
    return results


def main():
    hosts = load_hosts(HOSTS)
    scan_results = scan_hosts(hosts)
    print(scan_results)


if __name__ == "__main__":
    main()
