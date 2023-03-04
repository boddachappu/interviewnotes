class Singleton:
    __conn = None

    def __init__(self, name, age):
        if Singleton.__conn is None:
            self.name = name
            self.age = age
            Singleton.__conn = self
        else:
            raise Exception('We cannont create class')

    @staticmethod
    def getInstance():
        if Singleton.__conn != None:
            return Singleton.__conn
        Singleton()

    @staticmethod
    def print_data():
        print(f"Name {Singleton.__conn.name} age {Singleton.__conn.age}")


ob = Singleton('Vinod', 30)
print(ob)
print(ob.print_data())
ob1 = Singleton.getInstance()
print(ob1)
print(ob1.print_data())
ob2 = Singleton.getInstance()
print(ob2)
print(ob2.print_data())

"""
Output
<__main__.Singleton object at 0x000001F42786C450>
Name Vinod age 30
None
<__main__.Singleton object at 0x000001F42786C450>
Name Vinod age 30
None
<__main__.Singleton object at 0x000001F42786C450>
Name Vinod age 30
None

"""

""""
Builder
"""""

"""
reference https://www.youtube.com/watch?v=rzksTdmlu_s
The builder pattern is used to create objects when we have to use is when we are creting complex objects like
building a car. Which will require to build multiple parts. Few parts may not be useful based on the car model.
eg: basic model will have few parts and top end will have all models. To create a car object with this requirement
we cannot differentiate the car properties in constructor based on the model. it can be solved with builder pattern

Entity class : Object class [eg car]
Builder class : it will create object
"""


class Person:
    def __init__(self):
        self.name = None
        self.age = None
        self.address = None

    def __str__(self):
        return f"A person with name {self.name} with age {self.age} with address {self.address}"


class PersonBuilder():
    def __init__(self, person=Person()):
        self.person = person

    def setname(self, name):
        self.person.name = name
        return self  # we need to pass self so that it we can build next part/object in creating complex object

    def setage(self, age):
        self.person.age = age
        return self

    def setaddress(self, address):
        self.person.address = address
        return self

    def build(self):
        return self.person


ob = PersonBuilder()
person = ob.build()
print(person)
person = ob.setname('Vinod').setaddress('Bengaluru').build()
print(person)
print(ob.setage(30).build())
ob2 = PersonBuilder()
person2 = ob2.setname('Rashmi').setage(29).build()
print(person2)

"""
A person with name None with age None with address None
A person with name Vinod with age None with address Bengaluru
A person with name Vinod with age 30 with address Bengaluru
A person with name Rashmi with age 29 with address Bengaluru
"""

