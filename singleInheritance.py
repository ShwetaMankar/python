class company:
    def __init__(self):
        self.compName = "Google"
        self.ceoName = "Sundar Pichai"

    def compdetails(self):
        print("Parent company")
        print("Name -  ", self.compName)
        print("CEO - ", self.ceoName)


class subComapny(company):
    def __init__(self):
        company.__init__(self)
        self.name = "Alphabate Inc."
        self.ceo = self.ceoName

    def details(self):
        print("Sub company")
        print("Name _ ", self.name)
        print("CEO - ",self.ceo)


sub = subComapny()
sub.compdetails()
sub.details()