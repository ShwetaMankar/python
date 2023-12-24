class student:
    def __init__(self):
        self.name = "Shweta"
        self.marks = 89
        self.age = 19
        self.branch = "Computer"
        self.year = "Third Year"

    def details(self):
        print("Name of student is ",self.name)
        print("Marks =  ",self.marks)
        print("Age = ",self.age)
        print("Branch = ",self.branch)
        print("Year = ",self.year)

stud = student()
s = student()

stud.details()
s.age = 20
s.details()