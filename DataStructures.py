class Node:

    def __init__(self, data=None, pointer=None):
        self.data = data
        self.pointer = pointer

    def getPointer(self):
        return self.pointer

    def setPointer(self, new):
        self.pointer = new


class LL:

    def __init__(self):
        self.head = None

    def insertEnd(self, val):
        current = self.head
        while current.pointer is not None:
            current = current.getPointer()
        current.setPointer(Node(val))

    def insertMiddle(self, f, i):
        current = self.head
        if current:
            while current.data != f:
                current = current.getPointer()
            oldAddress = current.getPointer()
            new = Node(i)
            current.setPointer(new)
            new.setPointer(oldAddress)

    def inserStart(self, value):
        node = Node(value)
        node.pointer = self.head
        self.head = node

    def display(self):
        current = self.head
        if current:
            res = ''
            while current.pointer is not None:
                res += current.data
                current = current.getPointer()
            res += current.data
            return res


ob = LL()
ob.inserStart('a')
ob.insertEnd('c')
ob.insertMiddle('a', 'b')
ob.insertEnd('z')
ob.insertMiddle('c', 'd')
print(ob.display())


class Stack:

    def __init__(self):
        self.data = []

    def push(self, data):
        self.data.append(data)

    def pop(self):
        self.data.pop()

    def __str__(self):
        return "".join([str(val) for val in self.data])


ob = Stack()
ob.push(1)
ob.push(2)
ob.push(3)
ob.push(10)
print(ob)
ob.pop()
print(ob)


class Queue:

    def __init__(self):
        self.data = []

    def enQueue(self, data):
        self.data.append(data)

    def deQueue(self):
        self.data.pop(0)

    def __str__(self):
        return "".join([str(val) for val in self.data])


ob = Queue()
ob.enQueue(1)
ob.enQueue(2)
ob.enQueue(3)
ob.enQueue(10)
print(ob)
ob.deQueue()
print(ob)