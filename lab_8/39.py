class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def find(s, temp_sum):
            if temp_sum > target:
                return
            if temp_sum == target:
                s = sorted(s)
                if s not in result:
                    result.append(s)
                return

            for num in candidates:
                find(s + [num], temp_sum + num)

        find([], 0)
        return result