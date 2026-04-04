#Это файл 622 для лабораторной работы 2
class MyCircularQueue(object):
    def __init__(self, k):
        self.k = k                      # максимальный размер очереди
        self.queue = [0] * k            # массив фиксированного размера
        self.front = 0                  # указатель на начало очереди
        self.rear = -1                  # указатель на конец очереди
        self.size = 0                   # текущее количество элементов

    def enQueue(self, value):
        if self.isFull():
            return False
        
        # Циклическое перемещение rear
        self.rear = (self.rear + 1) % self.k
        self.queue[self.rear] = value
        self.size += 1
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        
        # Циклическое перемещение front
        self.front = (self.front + 1) % self.k
        self.size -= 1
        return True

    def Front(self):
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self):
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.k