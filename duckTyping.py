class infosys:
    def __init__(self):
        self.name = "Infosys Headstart Project (2020-21)"
        self.budget = "INR 1.55 cr"
        self.sector = "Education, Employability and Livelihood Enhancement"
        self.partner = "Infosys Foundation"
        self.location = "Delhi-Delhi, Bangalore-Karnataka"
    def projectdetails(self):
        print("Infosys Project")
        print("Name : ", self.name)
        print("Budget : ", self.budget)
        print("Project Sector : ", self.sector)
        print("Implementing Partners : ", self.partner)
class tcs:
    def __init__(self):
        self.name = "Contribution to TCS Foundation (2016-17)"
        self.budget = "INR 200.00  cr"
        self.sector = "Others"
        self.partner = "TCS Foundation"
        self.location = "pan-india-pan india"
    def projectdetails(self):
        print("This is TCS project details")
        print("Name : ", self.name)
        print("Budget : ", self.budget)
        print("Project Sector : ", self.sector)
        print("Implementing Partners : ", self.partner)

class csrProject:
    def projectmethod(self, a):
       a.projectdetails()

i = infosys()
t = tcs()
p = csrProject()

p.projectmethod(i)
print("___________________________________________________________________________________________")
p.projectmethod(t)


