class mahindra:
    def __init__(self):
        self.mahindraName = "mahindra XUV300 Turbo Sport"
        self.mahindraPrice = "10.35 Lakh"
        self.mahindraMileage = "18.2 kmpl"
        self.mahindraEngine = "1197cc"
        self.mahindraSafety = "5 Star (Global NCAP)"
        self.mahindraFuelType = "Petrol"
        self.mahindraSittingCapacity = "5 Seater"
    def keySpecification(self):
        print("Name : ", self.mahindraName)
        print("Price : ", self.mahindraPrice)
        print("Mileage : ", self.mahindraMileage)
        print("Engine : ", self.mahindraEngine)
        print("safety : ", self.mahindraSafety)
        print("Fuel type : ", self.mahindraFuelType)
        print("Sitting capactity : ", self.mahindraSittingCapacity)


class hyundai(mahindra):
    def __init__(self):
        mahindra.__init__(self)
        self.hyundaiName = "Hyundai Verna"
        self.hyundaiPrice = "9.14 Lakh"
        self.hyundaiMileage = "17.7 to 25 kmpl"
        self.hyundaiEngine = "998 to 1497cc"
        self.hyundaiFuelType = self.mahindraFuelType
        self.hyundaiSittingCapacity = self.mahindraSittingCapacity
    def hyundaikeySpecification(self):
        print("Name : ", self.hyundaiName)
        print("Price : ", self.hyundaiPrice)
        print("Mileage : ", self.hyundaiMileage)
        print("Engine : ", self.hyundaiEngine)
        print("Fuel type : ", self.hyundaiFuelType)
        print("Sitting capactity : ", self.hyundaiSittingCapacity)

class toyota(hyundai,mahindra):
    def __init__(self):
        mahindra.__init__(self)
        hyundai.__init__(self)
        self.toyotaName = "Toyota Urban Cruiser"
        self.toyotaPrice = "9.02 Lakh"
        self.toyotaMileage = "17 to 18.7 kmpl"
        self.toyotaEngine = "1462cc"
        self.toyotaSafety = "4 Star (Global NCAP)"
        self.toyotaFuelType = self.mahindraFuelType
        self.toyotaSittingCapacity =  self.hyundaiSittingCapacity
    def toyotaKeySpecification(self):
        print("Name : ", self.toyotaName)
        print("Price : ", self.toyotaPrice)
        print("Mileage : ", self.toyotaMileage)
        print("Engine : ", self.toyotaEngine)
        print("safety : ", self.toyotaSafety)
        print("Fuel type : ", self.toyotaFuelType)
        print("Sitting capactity : ", self.toyotaSittingCapacity)

t = toyota()
t.hyundaikeySpecification()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
t.keySpecification()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
t.toyotaKeySpecification()

