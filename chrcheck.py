password = input("Enter password : ")

flag1=0
flag2=0
flag3=0
flag4=0
if(len(password)>=8):
	for i in password:
		if(ord(i)>=65 and ord(i)<=90):
			flag1=1 	#for uppercase letter
			
		elif(ord(i)>=97 and ord(i)<=122):
			flag2=1		#for lowercase letter
			
		elif(ord(i)>=48 and ord(i)<=57):
			flag3=1		#for digit
			
		elif((ord(i)>=58 and ord(i)<=64)or(ord(i)>=33 and ord(i)<=47) or (ord(i)>=91 and ord(i)<=96) or(ord(i)>=123 and ord(i)<=126)):
			flag4=1			#for special symbol
	
	if(flag1==1 and flag2==1 and flag3==1 and flag4==1):
		print("Password is valid")
	else:
		print("Invalid Passwords")
	
else:
	print("Invalid password")