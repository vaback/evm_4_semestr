class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def find(index, s):
            if index == (len(nums)):
                result.append(s)
                return 
            find(index + 1, s + [nums[index]])
            find(index + 1, s)

        find(0, [])
        return result