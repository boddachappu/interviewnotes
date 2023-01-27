class PrivateExample:
    __private = 'Vinod' # private class attribute

    def __init__(self, name):
        self.__instancevariable = name + '4'  # private instance attribute

    def __privatemethod(self):  # private method
        print("i am in private method")
        return 1


ob = PrivateExample('Vinod')
# ob.__private # AttributeError: type object 'PrivateExample' has no attribute '__private'
# ob.__privatemethod()  # AttributeError: type object 'PrivateExample' has no attribute '__privatemethod'


print(ob._PrivateExample__private)
print(ob._PrivateExample__instancevariable)
print(ob._PrivateExample__privatemethod())
