def bill(*amt):
	sum =0 
	for i in amt:
		sum=sum+i
	print(sum)
	
	if(sum<1000):
		return sum
		#print("no discount")
	
	if(sum>1000 and sum<1500):
		discount = (5/100)*sum
		return sum-discount #here you will get discount
		#print("5% discount")
		
	elif(sum>1500 and sum<2000):
		discount = (7/100)*sum
		return sum-discount
		#print("7% discount ")
		
	elif(sum>2000):
		discount = (9/100)*sum
		return sum-discount
		#print("9% discount")

if(__name__ == "__main__"):
	amtWithDiscount = bill(600,700,450,780)
	print("Total paid bill after discount is ",amtWithDiscount)