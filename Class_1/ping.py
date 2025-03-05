import platform
import os

print("NORMAL ----->")
#normally
os.system("ping -c 1 -w 2 8.8.8.8")
print("REDIRECTING ----->")

#redirecting output output should be zero but mine's nothing may be because of visaul studio
print(os.system("ping -c 1 -w 2 8.8.8.8 > /dev/null 2>&1"))