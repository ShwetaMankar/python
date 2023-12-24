print("Enter marks of below subject ")
math = float(input("Maths : "))
marathi = float(input("Marathi : "))
english = float(input("English : "))
history = float(input("History : "))
science = float(input("Science : "))
hindi = float(input("Hindi : "))
geography = float(input("Geography : "))

per = ((math+marathi+english+history+science+hindi+geography)/700)*100

print("Percentage is ", per, "%")