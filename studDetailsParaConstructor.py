class student:
    def __init__(self,name,age,mark,branch,year):
        self.name = name
        self.age = age
        self.mark = mark
        self.branch = branch
        self.year = year

    def details(self):
        print("Name of student is ", self.name)
        print("Marks =  ", self.mark)
        print("Age = ", self.age)
        print("Branch = ", self.branch)
        print("Year = ", self.year)

s = student("Shweta",19,90,"Computer","Third Year")
s.details()
s2 = student("Shraddha",20,91,"ENTC","Second Year")
s2.details()
s2.year = "Third Year"
print("Details after updation : ")
s2.details()