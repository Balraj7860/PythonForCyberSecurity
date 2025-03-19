import platform
import os

ip = "127.0.0.1"
cmd = "ping -c 1 {ip}"
exit_code = os.system(cmd)
print(exit_code)