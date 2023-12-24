def marks(**m):
	lstName=[]
	lstPercent=[]
	for i in m:
		sum=0
		lstName.append(i)
		for j in m[i]:
			#print(j)
			sum = sum+j
		per=sum/5
		lstPercent.append(per)
	lstMaxPercent = max(lstPercent)
	"""print(lstPercent)
	print(lstName)
	print(lstMaxPercent)"""
	perDict = dict(zip(lstName,lstPercent))
	#print(perDict)
	for stud in perDict:
		if(perDict[stud] == lstMaxPercent):
				#print(stud,perDict[stud]) 
				return perDict, stud, perDict[stud]

				
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
	studPerDict,studTop,studPerDictTop = marks(shweta=[42,90,78,88,99],arti=[62,90,89,93,78],sayali=[89,90,99,89,87])
	print(studPerDict,studTop,studPerDictTop)
	
	amtWithDiscount = bill(600,700,450,780)
	print("Total paid bill after discount is ",amtWithDiscount)
	