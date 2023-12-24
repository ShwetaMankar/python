lst = ["Good", 34, 8, 23.5, 6, "Happy", "Day", 3.3, 7, 7.6, 8]
print(lst)
print(len(lst))
i=0
sum=0
while(i<len(lst)):
	
	if(type(lst[i])== int or type(lst[i])== float):
		sum += lst[i]
		
	i+=1
	
print("Sum of all integer and floating number in list is ",sum)