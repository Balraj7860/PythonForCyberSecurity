#!/usr/bin/env python3
def is_prime(numbsi47):
    if numbsi47 <= 1:
        return False
    for i in range(2, int(numbsi47**0.5) + 1):
        if numbsi47 % i == 0:
            return False
    return True

numberbsi47 = int(input("Enter a number between 1 and 100: "))
if numberbsi47 <= 0:
    print("Number less than 1.. **error**")
    exit
elif numberbsi47 > 100:
    print("Number greater than 100.. **error**")
    exit
else:
    if is_prime(numberbsi47):
        print(f"{numberbsi47} is a prime number.")
    else:
        print(f"{numberbsi47} is not a prime number.")