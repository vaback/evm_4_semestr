class Solution(object):
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # Динамическое программирование
        # dp[i] = максимальная сумма до дома i
        # dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        prev2 = 0  # dp[i-2]
        prev1 = 0  # dp[i-1]
        
        for num in nums:
            current = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = current
        
        return prev1