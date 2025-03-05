import platform
import os

print("NORMAL\n")
#normally
os.system("ping -c 1 -w 2 8.8.8.8")
print("\nREDIRECTING\n")

#redirecting output output should be zero but mine's nothing may be because of visaul studio
os.system("ping -c 1 -w 2 8.8.8.8 > /dev/null 2>&1")