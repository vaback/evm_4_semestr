class Solution(object):
    def topKFrequent(self, nums, k):
        # Шаг 1: Создаем хэш-таблицу для подсчета частот
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        # Шаг 2: Сортируем элементы по частоте (по убыванию)
        # items() возвращает пары (ключ, значение)
        # sort by value (freq) in reverse order
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        
        # Шаг 3: Берем первые k элементов
        result = []
        for i in range(k):
            result.append(sorted_items[i][0])
        
        return result