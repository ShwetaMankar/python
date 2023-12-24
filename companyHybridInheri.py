class parentCompany:
    def __init__(self):
        self.name = "Tata Group"
        self.employees = 935000
        self.revenue = "US$128 billion (FY 2022)"
        self.website = "www.tata.com"
        self.founder = "Jamsedji Tata"
        self.founded = 1868
    def details(self):
        print("Parent Comapny Name : ", self.name)
        print("Founder : ", self.founder)
        print("Founded : ", self.founded)
        print("Number of Employees :", self.employees)
        print("Revenue : ", self.revenue)
        print("Website : ", self.website)

class subCompany(parentCompany):
    def __init__(self):
        parentCompany.__init__(self)
        self.nameofcomp = "TCS"
        self.parentcmop = self.name
        self.employee = 606331
        self.website1 = "www.tcs.com"
    def details2(self):
        print("Sub Comapny Name : ", self.nameofcomp)
    def hr(self):
        print("Number of employees in TCS : ", self.employee)
    def sales(self):
        print("Revenue : ", self.revenue)
    def management(self):
        print("Website : ", self.website1)

class subCompany2(subCompany,parentCompany):
    def __init__(self):
        subCompany.__init__(self)
        parentCompany.__init__(self)
        self.nameofComp2 = "AirIndia"
        self.parentcmop = self.name
        self.employee = 28085
        self.website2 = "www.airindia.com"
        self.subFounded = 2007
        self.revenue2 = "US$1.8 billion (FY 2011)"

    def details3(self):
        print("Name : ", self.nameofComp2)
        print("Parent Comapny Name : ", self.parentcmop)
        print("Founded : ", self.subFounded)
        print("Number of Employees :", self.employee)
        print("Revenue : ", self.revenue2)
        print("Website : ", self.website2)


s = subCompany2()
s.details()
s.details2()
s.hr()
s.sales()
s.management()
s.details3()