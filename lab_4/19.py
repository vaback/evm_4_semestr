class Solution(object):
    def removeNthFromEnd(self, head, n):
        # Сначала найдем длину списка
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # Если нужно удалить первый элемент
        if n == length:
            return head.next
        
        # Найдем узел перед удаляемым
        current = head
        for i in range(length - n - 1):
            current = current.next
        
        # Удаляем узел
        current.next = current.next.next
        
        return head