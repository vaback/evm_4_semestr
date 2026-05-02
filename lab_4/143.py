class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return
        
        # Шаг 1: Находим середину списка (метод быстрого и медленного указателей)
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Шаг 2: Разворачиваем вторую половину списка
        prev = None
        current = slow
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        
        # Шаг 3: Сливаем две половины с чередованием
        first = head
        second = prev  # начало развёрнутой второй половины
        
        while second.next:
            # Сохраняем следующие узлы
            temp1 = first.next
            temp2 = second.next
            
            # Чередуем: first -> second -> first.next
            first.next = second
            second.next = temp1
            
            # Двигаем указатели
            first = temp1
            second = temp2