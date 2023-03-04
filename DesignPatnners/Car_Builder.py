class Car:

    def __init__(self):
        self.name = None
        self.model = None
        self.price = None
        self.display = None

    def __str__(self):
        return f"The car name {self.name} model {self.model} of price {self.price} and contains display {self.display}"


class CarBuilder:

    def __init__(self):
        self.car = Car()

    def setName(self, name):
        self.car.name = name
        return self

    def setModel(self, model):
        self.car.model = model
        return self

    def setPrice(self, price):
        self.car.price = price
        return self

    def setDisplay(self, display):
        self.car.display = display
        return self

    def carBuild(self):
        return self.car


carobj = CarBuilder()
print(carobj.carBuild())

fordfigo = CarBuilder()
print(fordfigo.setName("Figo").setModel("2011").setPrice("2.6L").carBuild())

fordfigohighend = CarBuilder()
print(fordfigohighend.setName("Figo").setModel("2011").setPrice("5.6L").setDisplay("Beauty").carBuild())
