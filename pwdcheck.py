pwd=input("Enter password : ")

flag1=0
flag2=0
flag3=0
flag4=0

if(len(pwd)>=8):
	for i in pwd:
		if(ord(i)>=65 and ord(i)<=90):	#uppercase
			flag1=1	
		if(ord(i)>=97 and ord(i)<=122):	#lowercase
			flag2=1
		if(ord(i)>=48 and ord(i)<=57): 	#digit
			flag3=1
		if((ord(i)>=58 and ord(i)<=64)or(ord(i)>=33 and ord(i)<=47)or(ord(i)>=91 and ord(i)<=96)or(ord(i)>=123 and ord(i)<=126)):	#symbol
			flag4=1
	if(flag1==1 and flag2==1 and flag3==1 and flag4==1):
		print("Valid pwd")
	else:
		print("Invalid pwd")
else:
	print("Invalid pwd")