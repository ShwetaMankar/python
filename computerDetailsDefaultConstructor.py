class computer:
    def __init__(self):
        self.name = "Dell"
        self.colour = "Silver"
        self.display = "15.6 FHD WVA display"
        self.processor = "11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz, 2419 Mhz, 4 Core(s) 8 Logical Processor(s)"
        self.ram = "8GB"
        self.storage = "1TB"

    def information(self):
        print("Name : ",self.name)
        print("Colour : ",self.colour)
        print("Dispay : ",self.display)
        print("Processor : ",self.processor)
        print("RAM : ",self.ram)
        print("Storage : ",self.storage)

pc = computer()
pc.information()
