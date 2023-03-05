class QueueDS:
    queue = []

    def enqueData(self, data):
        return self.queue.append(data)

    def dequeueData(self):
        return self.queue.pop(0)

    def __str__(self):
        return str(self.queue)

qob = QueueDS()
qob.enqueData('a')
qob.enqueData('b')
qob.enqueData('c')
qob.enqueData('d')
qob.enqueData('e')
print(qob)
qob.dequeueData()
print(qob)

