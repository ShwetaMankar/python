class parenCompany:
    def __init__(self):
        self.compName = "Alphabate Inc."
        self.ceoName = "Sundar Pichai"

    def compdetails(self):
        print("Parent company")
        print("Name -  ", self.compName)
        print("CEO - ", self.ceoName)
        print()

class subComapny(parenCompany):
    def __init__(self):
        parenCompany.__init__(self)
        self.subCompName = "Google"
        self.ceoOfSubCompany = self.ceoName

    def details1(self):
        print("Sub company")
        print("Name _ ", self.subCompName)
        print("CEO - ",self.ceoOfSubCompany)
        print()

class subsidiary(subComapny):
    def __init__(self):
        subComapny.__init__(self)
        self.name = "YouTube"
        self.ceoOfCompany = self.ceoOfSubCompany

    def details2(self):
        print("Subsidiary")
        print("Name _ ", self.name)
        print("CEO - ",self.ceoOfCompany)

c = subsidiary()
c.compdetails()
c.details1()
c.details2()