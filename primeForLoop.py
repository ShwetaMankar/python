num = int(input("Enter number : "))
flag=0

if(num == 0):
	print("Natural Number")
else:
	for i in range(2,num):
		if(num%i==0):
			flag=1
			break
	if(flag==1):
		print("Not prime")
	else:
		print("Prime")