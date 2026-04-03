#Это файл 622 для лабораторной работы 2
class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.k = k                      # максимальный размер очереди
        self.queue = [0] * k            # массив фиксированного размера
        self.front = 0                  # указатель на начало очереди
        self.rear = -1                  # указатель на конец очереди
        self.size = 0                   # текущее количество элементов

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        
        # Циклическое перемещение rear
        self.rear = (self.rear + 1) % self.k
        self.queue[self.rear] = value
        self.size += 1
        return True

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        
        # Циклическое перемещение front
        self.front = (self.front + 1) % self.k
        self.size -= 1
        return True

    def Front(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.size == 0

    def isFull(self):
        """
        :rtype: bool
        """
        return self.size == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()