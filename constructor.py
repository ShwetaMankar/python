class calculator:

    def __init__(self): # __init__ is constructor or special method in python
        self.a = 70
        self.b = 40
        print("This is special method in python i.e. constructor ")

    def add(self):
        print(self.a)
        print(self.a + self.b)

    def sub(self):
        print(self.a - self.b)

    def div(self):
        print(self.a / self.b)

    def mul(self):
        print(self.a * self.b)


cal = calculator()

cal.add()
cal.mul()
