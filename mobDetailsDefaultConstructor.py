class mobile:
    def __init__(self):
        self.name = "OPPO K3"
        self.colour = "Aurora Blue"
        self.display = "Amoled display"
        self.model = "CPH1955"
        self.ram = "8GB"
        self.storage = "128GB"
        self.battery = "3765MAH"

    def description(self):
        print("Name : ",self.name)
        print("Colour : ",self.colour)
        print("Dispay : ",self.display)
        print("Model : ",self.model)
        print("RAM : ",self.ram)
        print("Storage : ",self.storage)
        print("Battery : ",self.battery)

mob = mobile()
mob.description()

mob2 = mobile()
mob2.colour = "Jade Black"

print("Model with different colour ")
mob2.description()