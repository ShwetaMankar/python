i=0
Total_marks = 0
j=0
flag = 0
while(i<5):
	marks = float(input("Enter marks : "))
	Total_marks += marks
	if(marks < 35):
		flag = 1
		j+=1
		print("Fail in subject ",j)
	i+=1

marks_percentage = (Total_marks/500)*100
print("Total Marks of all sbjects : ",Total_marks)
print("Percentage of marks is ",marks_percentage)

if(j>2):
	print("fail")
elif(flag == 1):
	print("A.T.K.T.")
elif(marks_percentage > 35 and marks_percentage < 50):
	print("Third class")
elif(marks_percentage > 50 and marks_percentage < 75):
	print("Second class")
elif(marks_percentage > 75 and marks_percentage < 100):
	print("First class with distinction")