class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def find(s, nums_):
            if len(s) == len(nums):
                result.append(s)
                return

            for i in range(len(nums_)):
                find(s + [nums_[i]], nums_[:i] + nums_[i+1:])
        
        nums_ = nums.copy()
        find([], nums_)
        return result