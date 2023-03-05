class IteratorExample:
    def __init__(self, power):
        self.power = power
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.power:
            result = 2 ** self.count
            self.count += 1
            return result
        else:
            raise StopIteration


ob = IteratorExample(3)
print(next(ob))
print(next(ob))
print(next(ob))
print(next(ob))
