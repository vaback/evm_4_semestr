#875
class Solution(object):
    def minEatingSpeed(self, piles, h):
        # Функция проверки: успеет ли Коко съесть все бананы со скоростью k за h часов
        def can_finish(k):
            hours_needed = 0
            for pile in piles:
                hours_needed += (pile + k - 1) // k
                # Небольшая оптимизация: если уже превысили лимит h, дальше можно не считать
                if hours_needed > h:
                    return False
            return hours_needed <= h

        # Устанавливаем границы бинарного поиска
        left = 1
        right = max(piles)

        # Бинарный поиск
        while left < right:
            mid = (left + right) // 2
            if can_finish(mid):
                # Если с текущей скоростью успеваем, пробуем найти меньше
                right = mid
            else:
                # Если не успеваем, нужно есть быстрее
                left = mid + 1

        # left будет минимальной подходящей скоростью
        return left