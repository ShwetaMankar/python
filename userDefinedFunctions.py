def addition():
	addNum1 = int(input("Enter first number to do addition "))
	addNum2 = int(input("Enter second number to do addition "))
	
	add = addNum1+addNum2
	print("Addition is -> ",add)
	
	add2 = Num1+Num2
	print("Addition of global variables is -> ",add2)
	
def substraction():
	subNum1 = int(input("Enter first number to do substraction "))
	subNum2 = int(input("Enter second number to do substraction "))
	
	sub = subNum1-subNum2
	print("Substrsction is -> ",sub)
	
	sub2 = Num1-Num2
	print("Substrsction of global variables is -> ",sub2)
	
def multiplication():
	mulNum1 = int(input("Enter first number to do multiplication "))
	mulNum2 = int(input("Enter second number to do multiplication "))
	
	mul = mulNum1*mulNum2
	print("Multiplication is -> ",mul)
	
	mul2 = Num1*Num2
	print("Multiplication of global variables is -> ",mul2)
	
def division():
	divNum1 = int(input("Enter first number to do division "))
	divNum2 = int(input("Enter second number to do division "))
	
	div = divNum1/divNum2
	print("Division is -> ",div)
	
	
	div2 = Num1/Num2
	print("Division of global variables is -> ",div2)
	

Num1 = int(input("Enter first number "))
Num2 = int(input("Enter second number "))
	
addition()
substraction()
multiplication()
division()