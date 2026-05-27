# Network Host Availability Scanner

A simple, modular Python tool that loads a list of host IP addresses from a file, pings each host using ICMP echo requests, and reports whether each host is reachable. Designed as a lightweight network utility and a learning project for Python, networking fundamentals, and clean code structure.

## Features

- Load hosts from a text file
- Ping each host using pythonping
- Structured results (IP, status, latency)
- Modular, well‑documented functions

## How It Works

1. The program reads IP addresses from `data/hosts.txt`.
2. Each IP is pinged once using `pythonping`.
3. Results are stored in dictionaries containing:
   - `ip`
   - `status` (UP/DOWN)
   - `latency` (ms or -1)
4. Results are saved to a csv file.

## Example Code Snippet

```python
def ping_host(ip: str) -> dict:
    response = ping(ip, count=1)
    if response.success():
        latency = response.rtt_avg_ms
        return {"ip": ip, "status": "UP", "latency": latency}
    else:
        return {"ip": ip, "status": "DOWN", "latency": -1}
```

## hosts.txt Format

Each line should contain one IP address.

```
192.168.1.1
8.8.8.8
10.0.0.5
```

Blank lines are ignored.

## Example CSV Output

```
ip,status,latency_ms
192.168.1.1,UP,2.14
8.8.8.8,UP,18.52
10.0.0.5,DOWN,-1
```

## What I Learned

- Working with Python I/O
- Using third-party libraries (pythonping)
- Structuring a Python project with modular functions
- Basic network troubleshooting concepts
