class Solution(object):
    def generateParenthesis(self, n):
        result = []  # Здесь будем хранить все готовые комбинации
        
        def backtrack(current, left, right):
            # current: текущий список символов (например, ['(', '('])
            # left: сколько '(' уже использовали
            # right: сколько ')' уже использовали
            
            # Базовый случай: использовали все скобки
            if left == right == n:
                # Превращаем список в строку и добавляем в результат
                result.append(''.join(current))
                return
            
            # Правило 1: можем добавить '(' если ещё не использовали все
            if left < n:
                current.append('(')           # Добавляем
                backtrack(current, left + 1, right)  # Рекурсивно идём дальше
                current.pop()                 # Убираем (backtrack!)
            
            # Правило 2: можем добавить ')' если закрывающих меньше чем открывающих
            if right < left:
                current.append(')')           # Добавляем
                backtrack(current, left, right + 1)  # Рекурсивно идём дальше
                current.pop()                 # Убираем (backtrack!)
        
        backtrack([], 0, 0)  # Начинаем с пустого списка
        return result