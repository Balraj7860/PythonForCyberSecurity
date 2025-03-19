import platform 
import os

# ip_prefix = "192.168.1."

# for final_octet in range(254):
#     ip = ip_prefix + str(final_octet + 1)
#     cmd  = f"ping -c 1 -W 2 {ip} > nul"

#     exit_code = os.system(cmd)

#     if exit_code == 0:
#         print("{0} is online".format(ip))

ip_p = "192.168.1."

for i in range(254):
    ip = ip_p + str(i + 1)

    cmd  = f"ping -c 1 -W 2 {ip} > nul"

    exit_code = os.system(cmd)

    if(exit_code == 0):
        print(f"{ip} is online...")
        print(os.system("socket.gethost"))