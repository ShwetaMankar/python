def add(*a):
	sum = 0 
	for i in a:
		#print(i)
		sum = sum + i
	return sum

def sub(s1,s2):
	return s1-s2
def mul(m1,m2):
	return m1*m2
def div(d1,d2):
	return d1/d2

#print(__name__)
if(__name__ == "__main__"):
	a=add(1,2,3,4,5)
	print("Addition = ",a)
		
	s=sub(56,44)
	print("Substraction = ",s)

	m=mul(2,3)
	print("Multiplication = ",m)

	d=div(44,4)
	print("Division = ",d)