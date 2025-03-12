import nmap

target_address = "192.168.56.101"

port_start = 1
port_end = 100

scanner = nmap.PortScanner()

print("Scanning {0}".format(target_address))

for port in range(port_start, port_end + 1):
    result = scanner.scan(target_address, str(port))
    port_status = result['scan'][target_address]['tcp'][port]['state']
    print("\tPort: {0} is {1}".format(port, port_status))