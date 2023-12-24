class company:
    def __init__(self):
        self.name = "Google"
        self.ceoName = "Sundar Pichai"

    def compdetails(self):
        print("Parent company -  ", self.name)
        print("CEO - ",self.ceoName)

class subComapny(company):
    def __init__(self):
		self.name = "Alphabate Inc."
		company.__init__(self)
		
    def details(self):
        print("Sub Company _ ",self.name)
        #print("CEO - ",self.ceo2)

sub = subComapny()
sub.compdetails()
sub.details()