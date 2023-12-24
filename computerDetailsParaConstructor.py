class computer:
    def __init__(self,name,colour,display,processor,ram,storage):
        self.name = name
        self.colour = colour
        self.display = display
        self.processor = processor
        self.ram = ram
        self.storage = storage

    def information(self):
        print("Name : ",self.name)
        print("Colour : ",self.colour)
        print("Dispay : ",self.display)
        print("Processor : ",self.processor)
        print("RAM : ",self.ram)
        print("Storage : ",self.storage)

pc = computer("Dell","Silver","15.6 FHD WVA display","11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz, 2419 Mhz, 4 Core(s), 8 Logical Processor(s)","8GB","1TB")
pc.information()
print()
print("--------------------------------------------------------------------------------------------------")
pc2 = computer("Lenovo","Gray","15.6 FHD ","12th Gen Intel(R) Core(TM) i3-1215U Processor (E-cores upto 3.30 GHz P-cores up to 4.40 GHz)","8GB","512GB")
pc2.information()

pc2.colour = "Black"
print()
print("--------------------------------------------------------------------------------------------------")
print("Model with different colour ")
pc2.information()