list = [92,78, 28, 90, 34, 76, 100, 78, 45]
total_marks = len(list)*100
fail_in = 0
sum = 0 
flag = 0
marks_obtained = 0

for mark in list:
	if(mark<35):
		flag = 1
		fail_in +=1
	
	marks_obtained+=mark

percentage = (marks_obtained/ total_marks) *100

print("Total marks : ",total_marks)
print("Total marks obtained : ",marks_obtained)
print("Fail in ",fail_in,"subject")
print("Percentage : ",percentage)

if(fail_in>2):
	print("Fail")
elif(flag==1):
	print("A.T.K.T")
elif(percentage > 35 and percentage <50):
	print("Pass")
elif(percentage > 50 and percentage <75):
	print("Second class")
elif(percentage > 75 and percentage <100):
	print("First class with distinction")
	
