import os
# from datetime import datetime
import datetime

def w_log(message):
    now = str(datetime.datetime.now()) + "\t"
    message = now + str(message) + "\n"
    f = open("log_pingerrw.txt","a")
    f.write(message)
    f.close()

def importaddress():
    lines = []
    f = open("ipaddress.txt","r")
    for line in f:
        line = line.strip()
        lines.append(line)
    f.close()

    return lines
    
def ping(ip):
    cmd = f"ping -c 1 -W 2 {ip} > nul"
    exit_code = os.system(cmd)
    return exit_code



# __________________________________________________________

f = open("ipaddress.txt","w")
ip_prefix = "192.168.1."
for i in range(254):
    ip  = ip_prefix + str(i+1) + "\n"
    f.write(ip)
f.close()

print("\n** The file is ready **\n")

f = open("ipaddress.txt","r")
ip_address = importaddress()
print("Imported {0} ip address... ".format(len(ip_address)))
f.close()

for ip in ip_address:
    exit_code = ping(ip)

    if exit_code == 0:
        w_log("{0} is online...".format(ip))
        print("{0} is online...".format(ip))
    else:
        w_log("{0} is offline...".format(ip))
        # print("{0} is offline...".format(ip))
    
