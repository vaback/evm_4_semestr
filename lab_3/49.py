class Solution(object):
    def groupAnagrams(self, strs):
        from collections import defaultdict
        
        # Создаем словарь, где ключ - отсортированная строка, значение - список анаграмм
        anagrams = defaultdict(list)
        
        # Проходим по всем строкам
        for s in strs:
            # Сортируем строку, чтобы получить ключ
            # Для пустой строки sorted даст пустой список, который превратится в ""
            key = ''.join(sorted(s))
            anagrams[key].append(s)
        
        # Возвращаем все значения словаря
        return list(anagrams.values())