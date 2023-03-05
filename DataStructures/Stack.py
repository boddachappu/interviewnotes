class StackDS:
    stack = []

    def pushData(self, data):
        return self.stack.append(data)

    def popData(self):
        return self.stack.pop()

    def __str__(self):
        return str(self.stack)


qob = StackDS()
qob.pushData('a')
qob.pushData('b')
qob.pushData('c')
qob.pushData('d')
qob.pushData('e')
print(qob)
qob.popData()
print(qob)
