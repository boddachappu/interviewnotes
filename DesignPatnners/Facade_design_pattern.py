class Washing:
    def washing(self):
        print("washing")



class Rinsing:
    def rinsing(self):
        print("rinsing")


class Drying:
    def drying(self):
        print("drying")



class WashingMachineFacade:

    def __init__(self):
        self.wash = Washing()
        self.rinse = Rinsing()
        self.dry = Drying()


    def washing(self):
        self.wash.washing()
        self.rinse.rinsing()
        self.dry.drying()


facade_obj = WashingMachineFacade()
facade_obj.washing()