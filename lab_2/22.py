class Solution(object):
    def generateParenthesis(self, n):
        result = []
        
        def backtrack(current, left, right):
            # Если использовали все скобки - сохраняем результат
            if left == n and right == n:
                result.append(current)
                return
            
            # Добавляем открывающую скобку, если можно
            if left < n:
                backtrack(current + '(', left + 1, right)
            
            # Добавляем закрывающую скобку, если можно
            if right < left:
                backtrack(current + ')', left, right + 1)
        
        backtrack("", 0, 0)
        return result