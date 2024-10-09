from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        used = set()

        def backtracking(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return

            for i in nums:
                if i in used:
                    continue
                used.add(i)

                backtracking(curr + [i])
                used.remove(i)

        backtracking([])

        return ans