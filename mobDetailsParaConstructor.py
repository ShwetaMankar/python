class mobile:
    def __init__(self,name,colour,display,processor,ram,storage,battery):
        self.name = name
        self.colour = colour
        self.display = display
        self.processor = processor
        self.ram = ram
        self.storage = storage
        self.battery = battery

    def description(self):
        print("Name : ",self.name)
        print("Colour : ",self.colour)
        print("Dispay : ",self.display)
        print("Processor : ",self.processor)
        print("RAM : ",self.ram)
        print("Storage : ",self.storage)
        print("Battery : ",self.battery)

mob = mobile("VIvo V23 5G","Sunshine gold","Full HD + display","Octa core","8GB","128GB","4300 mAh Battery")
mob.description()
print()
print("--------------------------------------------------------------------------------------------------")
mob2 = mobile("Realme C33","Sandy gold","LCD, 60 Hz Refresh rate ","Octa core","4GB","64GB","5000 mAh Battery")
mob2.description()

mob2.colour = "Night Sea"
print()
print("--------------------------------------------------------------------------------------------------")
print("Model with different colour ")
mob2.description()