class Solution(object):
    def isValid(self, s):
        bracket_map = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []

        for char in s:
            if char in bracket_map:          # если char — открывающая скобка
                stack.append(char)           # кладём её в стек
            else:                            # иначе это закрывающая скобка
                if not stack:                # если стек пуст — нет открывающей
                    return False
                top_element = stack.pop()    # берём последнюю открывающую
                if bracket_map[top_element] != char:  # проверяем соответствие
                    return False

        return not stack   # True, если стек пуст (все скобки закрыты)