class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # Фиктивный узел для упрощения построения результирующего списка
        dummy = ListNode(0)
        current = dummy
        carry = 0  # перенос
        
        # Продолжаем, пока есть цифры в l1, l2 или есть перенос
        while l1 is not None or l2 is not None or carry != 0:
            # Получаем значения текущих разрядов
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            
            # Вычисляем сумму и перенос
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            
            # Создаем новый узел с полученной цифрой
            current.next = ListNode(digit)
            current = current.next
            
            # Переходим к следующим узлам
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        
        return dummy.next