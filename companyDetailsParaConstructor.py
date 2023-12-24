class company:
    def __init__(self,name,founder,founded,revenue):
        self.name = name
        self.founder = founder
        self.founded = founded
        self.revenue = revenue

    def compInfo(self):
        print("Name : ",self.name)
        print("Founder : ", self.founder)
        print("Founded : ",self.founded)
        print("Revenue : ",self.revenue)

c = company("Wipro","Muhammed Hashim Premji",1945,"US$10 billion (2022)")
c2 = company("Amazon","Jeff Bezos",1994,"UD$469.822 billion (2021)")
c.compInfo()
c2.compInfo()
