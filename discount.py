a = float(input("Enter total price : "))

if(a>1000 and a<1500):
	print("5% discount")
	discount = (5/100)*a
	print("Discount on given amount is ",discount)
elif(a>1500 and a<2000):
	print("7% discount ")
	discount = (7/100)*a
	print("Discount on given amount is ",discount)
elif(a>2000):
	print("9% discount")
	discount = (9/100)*a
	print("Discount on given amount is ",discount)