lst=[0,-1,0,0]
max = lst[0]
for i in range(1,len(lst)):
	if(lst[i]>max):
		max=lst[i]

print("Max number is ",max)
