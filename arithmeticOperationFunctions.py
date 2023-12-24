def addition():
	return num1+num2
def substraction():
	return num1-num2
def multiplication():
	return num1*num2
def division():
	return num1/num2
def totalOf():
	total = a+s+m+d
	return total

num1 = float(input("First number : "))
num2 = float(input("Second number : "))

a = addition()
print("Addition of num1 and num2 is ",a)
s = substraction()
print("Substraction of num1 and num2 is ",s)
m = multiplication()
print("Multiplication of num1 and num2 is ",m)
d = division()
print("Division of num1 and num2 is ",d)
t = totalOf()
print("Total of values returned by functions is ",t)

