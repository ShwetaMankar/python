def marks(*student_marks):
	
	for single_student_mark in student_marks:
		#print(single_student_mark)
		print("-----------------")
		total_marks = 0
		total_marks_obtained=0
		flag=0
		fail_in_subject=0
		for each_subject_mark in single_student_mark:
			print(each_subject_mark)
			if each_subject_mark < 35:
				flag = 1
				fail_in_subject=fail_in_subject+1
			
			total_marks_obtained = total_marks_obtained + each_subject_mark
			total_marks = total_marks + 100
			
		
		
		percentage = (total_marks_obtained/total_marks)*100 
		
		print("Total Marks Obtained = ",total_marks_obtained)
		print("Total Marks = ",total_marks)
		print("Percentage = ",percentage,"%")
		
		if fail_in_subject > 1:
			print("fail")
		elif flag==1:
			print("ATKT")
		elif percentage > 35 and percentage<60:
			print("Pass")
		elif percentage > 60 and percentage < 75:
			print("Second class")
		elif percentage > 75 and percentage < 100:
			print("First class with distinction")

marks([89,99,87,27,90],[45,90,89,99,83],[67,87,34,56,34],[90,99,98,96,87],[35,87,98,54,87])