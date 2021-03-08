from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        output = []

        for i in range(n):
            output.append(nums[i])
            output.append(nums[n + i])

        return output

print(Solution().shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4))
