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

		
if(__name__ == "__main__"):		
	studPerDict,studTop,studPerDictTop = marks(shweta=[42,90,78,88,99],arti=[62,90,89,93,78],sayali=[89,90,99,89,87])
	print(studPerDict,studTop,studPerDictTop)
	