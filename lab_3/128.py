class Solution(object):
    def longestConsecutive(self, nums):
        # Создаем хэш-таблицу (множество) для O(1) поиска
        num_set = set(nums)
        longest_streak = 0
        
        # Проходим по каждому числу
        for num in num_set:
            # Проверяем, является ли текущее число началом последовательности
            # Начало последовательности - это число, у которого нет левого соседа (num - 1)
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                # Расширяем последовательность вправо
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                # Обновляем максимальную длину
                longest_streak = max(longest_streak, current_streak)
        
        return longest_streak