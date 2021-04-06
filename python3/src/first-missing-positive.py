from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        values = set()
        i = minPos = 1
        for n in nums: # O(N)
            if n > 0:
                values.add(n)
                minPos = min(minPos, n)

        i = minPos
        while i < minPos + len(nums):
            if i not in values:
                return i
            i += 1

        return i

#print(Solution().firstMissingPositive([]))
print(Solution().firstMissingPositive([1]))
#print(Solution().firstMissingPositive([1,2,0]))