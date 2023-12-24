t=(1,33,44,66,234,33,1,2)
a=list(t)
for i in range(len(a)):
	if t.count(i>1):
		count=a.count(i)
	a[i]=int(a[i])
	
print(i,"appears",count,"times in tuple")