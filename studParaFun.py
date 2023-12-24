def studentResult(marathi,hindi,english,math,science):
	Total_marks=marathi+hindi+english+math+science
	
	
	#Total_marks = 0
	
	flag = 0
	"""j=0
	i=0
	while(i<5):
		marks = float(input("Enter marks : "))
		Total_marks += marks
		if(marks < 35):
			flag = 1
			j+=1
			print("Fail in subject ",j)
		i+=1"""

	marks_percentage = (Total_marks/500)*100
	print("Total Marks of all sbjects : ",Total_marks)
	print("Percentage of marks is ",marks_percentage)

	if(marks_percentage<35):
		return fail
	elif(flag == 1):
		return "A.T.K.T."
	elif(marks_percentage > 35 and marks_percentage < 50):
		return "Third class"
	elif(marks_percentage > 50 and marks_percentage < 75):
		return "Second class"
	elif(marks_percentage > 75 and marks_percentage < 100):
		return "First class with distinction"
		
	#return Total_marks,marks_percentage
		
	
f=studentResult(33,33,33,33,33)
print(f)
studentResult(94,83,89,76,88)	
"""studentResult(96,44,98,57,98)
studentResult(44,33,29,56,68)
studentResult(94,83,89,76,88)
studentResult(97,99,78,99,96)"""
