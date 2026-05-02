class Solution(object):
    def reverseList(self, head):
        prev = None
        current = head
        
        while current:
            next_temp = current.next  # сохраняем ссылку на следующий узел
            current.next = prev        # разворачиваем указатель
            prev = current             # двигаем prev вперед
            current = next_temp        # двигаем current вперед
        
        return prev  # prev теперь указывает на новую голову списка