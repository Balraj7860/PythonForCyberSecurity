#!/usr/bin/env python3
def reverse_while_loop(sbsi47):
    s1bsi47 = ''
    lengthbsi47 = len(sbsi47) - 1
    while lengthbsi47 >= 0:
        s1bsi47 = s1bsi47 + sbsi47[lengthbsi47]
        lengthbsi47 = lengthbsi47 - 1
    return s1bsi47

input_strbsi47 = ['W4$acxyH7BtQiU3er','Zk7i$F8uo#Aq','L#1npOdATe2rjy','vE@XsLwzKmy','cBa6Hg7@uY3WjR','QpiTcS7Ozlk2']

for i in range(len(input_strbsi47)):
    print('Reverse String using while loop =', reverse_while_loop(input_strbsi47[i]))