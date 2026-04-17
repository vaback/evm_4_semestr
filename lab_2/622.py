class MyCircularQueue(object):
    def __init__(self, k):
        self.k = k                    # максимальный размер
        self.push_stack = []          # стек для добавления
        self.pop_stack = []           # стек для удаления
        self.size = 0                 # текущий размер
    
    def enQueue(self, value):
        """Добавляет элемент в конец"""
        if self.isFull():
            return False
        
        self.push_stack.append(value)
        self.size += 1
        return True
    
    def deQueue(self):
        """Удаляет элемент из начала"""
        if self.isEmpty():
            return False
        
        # Если pop_stack пуст, перекладываем всё из push_stack
        if not self.pop_stack:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())
        
        self.pop_stack.pop()
        self.size -= 1
        return True
    
    def Front(self):
        """Возвращает первый элемент"""
        if self.isEmpty():
            return -1
        
        # Если pop_stack пуст, перекладываем
        if not self.pop_stack:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())
        
        return self.pop_stack[-1]
    
    def Rear(self):
        """Возвращает последний элемент"""
        if self.isEmpty():
            return -1
        
        # Если push_stack не пуст, последний добавленный — в нём
        if self.push_stack:
            return self.push_stack[-1]
        
        # Иначе последний элемент — в pop_stack (самый первый в нём)
        return self.pop_stack[0]
    
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.k