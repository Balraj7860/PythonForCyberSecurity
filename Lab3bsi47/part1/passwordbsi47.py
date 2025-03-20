#!/usr/bin/env python3

def password_check(passwdbsi47):
	
	SpecialSymbsi47 =['$', '@', '#']
	valbsi47 = True
	
	if len(passwdbsi47) < 6:
		print('length should be at least 6')
		valbsi47 = False
		
	if len(passwdbsi47) > 20:
		print('length should be not be greater than 8')
		valbsi47 = False
		
	if not any(char.isdigit() for char in passwdbsi47):
		print('Password should have at least one numeral')
		valbsi47 = False
		
	if not any(char.isupper() for char in passwdbsi47):
		print('Password should have at least one uppercase letter')
		valbsi47 = False
		
	if not any(char.islower() for char in passwdbsi47):
		print('Password should have at least one lowercase letter')
		valbsi47 = False
		
	if not any(char in SpecialSymbsi47 for char in passwdbsi47):
		print('Password should have at least one of the symbols $@#')
		valbsi47 = False
	if valbsi47:
		return valbsi47

def main():
	passwd = ['W4$acxyH7BtQiU3er','Zk7i$F8uo#Aq','L#1npOdATe2rjy','vE@XsLwzKmy','cBa6Hg7@uY3WjR','QpiTcS7Ozlk2']
	
    # for i in range(len(passwd)):
	#     if (password_check(passwd[i])):
	# 	    print("Password is valid")
	#     else:
	# 	    print("Invalid Password !!")
		
# Driver Code	 
if __name__ == '__main__':
	main()
