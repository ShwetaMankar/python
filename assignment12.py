string = input("Enter String : ")

str=""
a = ""
c = ""
d = ""
b = ""

for i in string:
	if(ord(i)>=65 and ord(i)<=90):#for uppercase letter
		print(ord(i))
		b+=i
		
	elif(ord(i)>=97 and ord(i)<=122):#for lowercase letter
		a+=i
		
	elif(ord(i)>=48 and ord(i)<=57):#for digit
		c+=i
		
	elif((ord(i)>=58 and ord(i)<=64)or(ord(i)>=33 and ord(i)<=47) or (ord(i)>=91 and ord(i)<=96) or(ord(i)>=123 and ord(i)<=126)):#for special symbol
		d+=i	

str=b+a+c+d
print(str)

	