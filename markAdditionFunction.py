def markAddition():
	marathi = float(input("Marathi Marks : "))
	hindi = float(input("Hindi Marks : "))
	english = float(input("English Marks : "))
	science = float(input("Science Marks : "))
	math = float(input("Math Marks : "))
	
	total= marathi+ hindi+ english+ science+ math
	
	return total

t = markAddition()
print("Marks of all subjects are ",t)
