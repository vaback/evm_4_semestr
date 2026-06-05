class Solution(object):
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        
        n = len(nums)
        # dp[i] = длина наибольшей возрастающей подпоследовательности,
        # заканчивающейся на nums[i]
        dp = [1] * n
        
        # Для каждого элемента ищем все предыдущие меньшие элементы
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)