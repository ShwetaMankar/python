class vivo:
    def __init__(self):
        self.vivoName = "Vivo V23 5G"
        self.vivoColour = "Sunshine gold"
        self.vivoDisplay = "Full HD + display"
        self.vivoRam = "8GB"
        self.vivoStorage = "128GB"
        self.vivoProcessor = "Octa core"
        self.vivoBattery = "4300 mAh Battery"

    def vivoDescription(self):
        print("Name : ",self.vivoName)
        print("Colour : ",self.vivoColour)
        print("Dispay : ",self.vivoDisplay)
        print("RAM : ",self.vivoRam)
        print("Storage : ",self.vivoStorage)
        print("Battery : ",self.vivoBattery)
        print("Processor : ",self.vivoProcessor)

class oppo(vivo):
    def __init__(self):
        vivo.__init__(self)
        self.oppoName = "OPPO K3"
        self.oppoColour = "Aurora Blue"
        self.oppoDisplay = "Amoled display"
        self.oppoModel = "CPH1955"
        self.oppoRam = self.vivoRam
        self.oppoStorage = self.vivoStorage
        self.oppoBattery = "3765MAH"
    def oppoDescription(self):
        print("Name : ",self.oppoName)
        print("Colour : ",self.oppoColour)
        print("Dispay : ",self.oppoDisplay)
        print("Model : ",self.oppoModel)
        print("RAM : ",self.oppoRam)
        print("Storage : ",self.oppoStorage)
        print("Battery : ",self.oppoBattery)

class realme(oppo,vivo):
    def __init__(self):
        vivo.__init__(self)
        oppo.__init__(self)
        self.realmeName = "Realme C33"
        self.realmeColour = "Sandy gold"
        self.realmeDisplay = "LCD, 60 Hz Refresh rate"
        self.realmeModel = "CPH1955"
        self.realmeRam = self.oppoRam
        self.realmeStorage = self.vivoStorage
        self.realmeProcessor = self.vivoProcessor
        self.realmeBattery = "5000 mAh Battery"
    def relmeDescription(self):
        print("Name : ",self.realmeName)
        print("Colour : ",self.realmeColour)
        print("Dispay : ",self.realmeDisplay)
        print("Model : ",self.realmeModel)
        print("RAM : ",self.realmeRam)
        print("Storage : ",self.realmeStorage)
        print("Battery : ",self.realmeBattery)
        print("Processor : ",self.realmeProcessor)

op = realme()
op.oppoDescription()
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
op.vivoDescription()
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
op.relmeDescription()