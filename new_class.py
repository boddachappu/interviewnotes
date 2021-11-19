class Example:
    count = 0
    __imp = 'Private Variable'

    def __init__(self, name):
        self.name = name

    def __iter__(self):
        return self.count

    def __next__(self):
        if self.count < len(self.name):
            res = self.count
            self.count += 1
            return res
        else:
            pass

    @staticmethod
    def happy():
        return 'I am happy '

    @classmethod
    def morehappy(cls, a, b):
        name = a + ' ' + b
        return cls(name)

    def happycheck(self):
        return 'instance method ' + self.name

    @property
    def namemethod(self):
        return self.name

    @namemethod.setter
    def namemethod(self,a):
        self.name = self.name + a


# ob = Example('vinod')
# print(next(ob))
# for i in range(10):
#     print(next(ob))
# print(ob.happy())
# print(Example.happy())
ob2 = Example.morehappy('vinod', 'rashmi')
print(ob2.name)
print(ob2.happy())
print(ob2.happycheck())
print(ob2._Example__imp)
ob3 = Example('vinod')
print(ob3.namemethod)
ob3.namemethod=' rashmi123'
print(ob3.name)
print(ob3._Example__imp)