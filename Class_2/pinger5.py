import platform
import os

def ping_host(ip):
    ping_cmd = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"
    exit_code = os.system(ping_cmd)
    return exit_code

def import_addresses():
    line = []
    f = open("ips.txt","r")
    for line in f:
        line = line.strip()
        line.append(line)
    return license

ip_addresses = import_addresses()

for ip in ip_addresses:
    exit_code = ping_host(ip)

    if exit_code == 0:
        print("{0} is online".format(ip))