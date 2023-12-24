class dell:
    def __init__(self):
        self.dellName = "Dell"
        self.dellColour = "Silver"
        self.dellRam = "8GB"
        self.dellStorage = "1TB"
        self.dellProcessor = "11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz, 2419 Mhz, 4 Core(s), 8 Logical Processor(s)"

    def dellConfiguration(self):
        print("Name : ",self.dellName)
        print("Colour : ",self.dellColour)
        print("RAM : ",self.dellRam)
        print("Storage : ",self.dellStorage)
        print("Processor : ",self.dellProcessor)

class hp(dell):
    def __init__(self):
        dell.__init__(self)
        self.hpName = "HP"
        self.hpColour = "Black"
        self.hpRam = self.dellRam
        self.hpStorage = self.dellStorage
        self.hpProcessor = self.dellProcessor
    def hpConfiguration(self):
        print("Name : ",self.hpName)
        print("Colour : ",self.hpColour)
        print("RAM : ",self.hpRam)
        print("Storage : ",self.hpStorage)
        print("Processor : ",self.hpProcessor)

class lenovo(hp,dell):
    def __init__(self):
        dell.__init__(self)
        hp.__init__(self)
        self.lenovoName = "Lenovo"
        self.lenovoColour = self.dellColour
        self.lenovoRam = self.hpRam
        self.lenovoStorage = "512GB"
        self.lenovoProcessor = "12th Gen Intel(R) Core(TM) i3-1215U Processor (E-cores upto 3.30 GHz P-cores up to 4.40 GHz)"
    def lenovoConfiguration(self):
        print("Name : ",self.lenovoName)
        print("Colour : ",self.lenovoColour)
        print("RAM : ",self.lenovoRam)
        print("Storage : ",self.lenovoStorage)
        print("Processor : ",self.lenovoProcessor)

pc = lenovo()
pc.dellConfiguration()
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
pc.hpConfiguration()
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
pc.lenovoConfiguration()