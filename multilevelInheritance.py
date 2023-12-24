class producer:
    def __init__(self):
        self.energyL1 = "energy"
        self.producer = "Tree"
    def produce(self):
        print("Producers are ", self.producer, "It consumes ",self.energyL1,"from Sun")
        print()

class primaryConsumer(producer):
    def __init__(self):
        producer.__init__(self)
        self.energyL2 = self.energyL1
        self.primary_Consumer = "Rabbit"
    def consume1(self):
        print("Primary Consumer is ",self.primary_Consumer,"It consumes ",self.energyL2," from ",self.producer)
        print()

class secondaryConsumer(primaryConsumer):
    def __init__(self):
        primaryConsumer.__init__(self)
        self.energyL3 =  self.energyL2
        self.secondary_Consumer = "Snake"
    def consume2(self):
        print("Secondary Consumer is ",self.secondary_Consumer,"It consumes ",self.energyL3," from ",self.primary_Consumer)

sc = secondaryConsumer()
sc.produce()
sc.consume1()
sc.consume2()
