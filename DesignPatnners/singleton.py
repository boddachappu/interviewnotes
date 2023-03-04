import logging


class Singleton(object):
    __instance = None
    logger = logging.getLogger(__name__)

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            val = super(Singleton, cls).__new__(cls)
            cls.__instance = val
        return cls.__instance

    def __init__(self):
        if Singleton.__instance is None:
            Singleton.__instance = self

    @staticmethod
    def singleton():
        if Singleton.__instance is not None:
            return Singleton.__instance
        return Singleton()

ob = Singleton()
print(ob._Singleton__instance)
print(id(ob.logger))
print(id(ob))
ob2 = Singleton()
print(id(ob2.logger))
print(id(ob2))


class Singleton:
    __instance = None

    def __init__(self):
        """ Virtually private constructor. """
        if Singleton.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance


s = Singleton()
print(s)

s = Singleton.getInstance()
print(s)

s = Singleton.getInstance()
print(s)


class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        """

        # ...


if __name__ == "__main__":
    # The client code.

    s1 = Singleton()
    s2 = Singleton()
    print(s1, s2)
    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")


class Logger(object):
    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            print('Creating new instance')
            cls._instance = cls.__new__(cls)
            # Put any initialization here.
        return cls._instance
