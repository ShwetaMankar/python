def markAddition(mark,n):
	avg = (mark)/n
	return avg

num = int(input("Enter number subject you want to get marks of : "))
sumofMark=0
for i in range(num):
		mark = float(input(" Subject Marks : "))
		sumofMark=mark+sumofMark
		i=+1
		

m = markAddition(sumofMark,num)
print("Average is ",m)
