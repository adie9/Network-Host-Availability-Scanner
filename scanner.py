from pythonping import ping

HOSTS = "data/hosts.txt"
OUTPUT = "output.txt"


def load_hosts(file_path):
    with open(file_path, "w") as f:
        hosts = []
        for line in f:
            line.strip()
            if line:
                hosts.append(line)
    return hosts


def ping_hosts(ip):
    response = ping(ip, verbose=True)
    if response.success():
        print("The ping was successful!")
    else:
        print("The ping failed. Host was unreachable.")


def main():
    pass


if __name__ == "__main__":
    main()
