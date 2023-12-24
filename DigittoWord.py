def Value(digit):
	if digit=='1':
		print("One", end=" ")
	elif digit=='2':
		print("Two", end=" ")
	elif digit=='3':
		print("Three", end=" ")
	elif digit=='4':
		print("Four", end=" ")

def word(n):
	i=0
	length=len(n)
	while i<length:
		Value(n[i])
		i+=1
n='1234'
word(n)