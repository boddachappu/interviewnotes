class CheckProperty:

    def __init__(self, name):
        self.name = name

    @property
    def checkname(self):
        return self.name

    @checkname.setter
    def checkname(self, value):
        self.name = value
        return self.name


ob = CheckProperty('Vinod')
print(ob.checkname)
ob.checkname = 'Rashmi'
print(ob.checkname)