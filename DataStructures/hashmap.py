class HashMap:
    def __init__(self, length):
        self.length = length
        self.data = {}


    def insertHash(self, key, value):
        idx =  hash(key) % self.length
        self.data[idx] = value


    def display(self, key):
        idx = hash(key) % self.length
        return self.data[idx]

    def __str__(self):
        return self.data


ob = HashMap(20)
print(ob.insertHash(10,20))
print(ob.insertHash(11,20))
print(ob.insertHash(12,1))
print(ob.insertHash(5,3))
print(ob.data)
print(ob.display(10))