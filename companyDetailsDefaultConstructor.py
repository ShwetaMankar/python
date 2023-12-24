class company:
    def __init__(self):
        self.name = "TCS"
        self.founder = "Tata sons"
        self.founded = 1968
        self.revenue = "US$25 billion"

    def compInfo(self):
        print("Name : ",self.name)
        print("Founder : ", self.founder)
        print("Founded : ",self.founded)
        print("Revenue : ",self.revenue)

c = company()
c.compInfo()
c.revenue = "US$128 billion(2021-22)"
print("Details after updation : ")
c.compInfo()