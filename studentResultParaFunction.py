def studentResult(marathi,hindi,english,math,science):
	Total_marks=marathi+hindi+english+math+science
	marks_percentage = (Total_marks/500)*100
	print("Total Marks of all sbjects : ",Total_marks)
	print("Percentage of marks is ",marks_percentage)

	if(marks_percentage<35):
		print("fail")
	elif(marks_percentage > 35 and marks_percentage < 50):
		print("Third class")
	elif(marks_percentage > 50 and marks_percentage < 75):
		print("Second class")
	elif(marks_percentage > 75 and marks_percentage < 100):
		print("First class with distinction")
		
studentResult(94,83,89,76,88)
print()	
studentResult(96,44,98,57,98)
print()	
studentResult(44,33,29,56,68)
print()	
studentResult(94,83,89,76,88)
print()	
studentResult(97,99,78,99,96)
