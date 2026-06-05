class Solution(object):
    def coinChange(self, coins, amount):
        # Базовый случай
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        
        # dp[i] = минимальное количество монет для суммы i
        # Инициализируем бесконечностью (большим числом)
        INF = float('inf')
        dp = [INF] * (amount + 1)
        dp[0] = 0  # Для суммы 0 нужно 0 монет
        
        # Заполняем dp для всех сумм от 1 до amount
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    # Если можем использовать текущую монету
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # Если dp[amount] осталась бесконечностью - значит невозможно собрать сумму
        return dp[amount] if dp[amount] != INF else -1