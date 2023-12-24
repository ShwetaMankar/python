f = open("myintro.txt","w")  # file in write mode
f.write("My name is Shweta Vijay Mankar.")
f.close

f = open("myintro.txt","a")		# file in append mode
f.write("I am studying Computer Engineering. ")
f.close

f = open("myintro.txt","r")		# file in read mode
print(myintro.read())
f.close

