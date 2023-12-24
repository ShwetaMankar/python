table_from = int(input("From where tables should start : "))
table_upto = int(input("Tables upto : "))

for i in range(table_from,table_upto+1):
	print()
	print("===== Table Of ",i,"=====")
	print()
	for j in range(1,11):
		print("	",i*j)