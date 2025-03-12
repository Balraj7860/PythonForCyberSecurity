import platform
import os

# ip_prefix = "192.168.0"
# current_os = platform.system().lower()

# for final_octet in range(254):
#     ip = ip_prefix +str(final_octet + 1)
#     if current_os == "windows":
#         ping_cmd = f"ping -n 1 -w 2 {ip} > nul"
#     else:
#         ping_cmd = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"
    
#     exit_code = os.system(ping_cmd)

#     if exit_code == 0:
#         print("{0} is online".format(ip))

ip_prefix = "192.168.0."

start_ip = int(input("Enter the starting ip:"))
if start_ip <=0:
    print("it should be greater than 0...")
    exit
end_ip = int(input("Enter the ending ip:"))
if end_ip >=255:
    print("it should be less than 255...")
    exit

for start_ip in range(end_ip):
    ip = ip_prefix + str(start_ip + 1)
    cmd = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"
    status = os.system(cmd)
    if status == 0:
        print("{0} is online...".format(ip))

a= '192.168.0.1'
b= a.split('.')
c = '.'.join(b)
print(b)
print(c)