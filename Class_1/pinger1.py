import os
cmd = f"ping -c 1 -w 2 192.168.56.101 > /dev/null 2>&1"
s = os.system(cmd)
print(s)