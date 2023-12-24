def productOf():
	start = int(input("Enter starting point of range : "))
	end = int(input("Enter ending point of range : "))
	product=1
	for i in range(start, end+1):
		if(i%2==0):
			product=product*i
	return product
		


productOfAll = productOf()
print("Product of all even values in given range is ",productOfAll)