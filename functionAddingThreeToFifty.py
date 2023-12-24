def addition():
	start = int(input("Enter starting value fors addition : "))
	end = int(input("Enter ending value for addition : "))
	sum=0
	for i in range(start, end):
		sum=sum+i
	print("Addition of given range is ",sum)
		
	
addition()