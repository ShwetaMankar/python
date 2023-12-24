import array 
a = array.array("i",[10,90,89,99,90,])
print(a)
a.insert(0,78)
print("Array after inserting element : ",a)
print("Maximum number in array is ",max(a))
print("Minimum number in array is ",min(a))


sum=0
for i in a:
	sum=sum+i
	if(i%2==0):
		print(i,"is even")
	else:
		print(i,"is odd")

print("Addition of all array elements is ",sum)

		