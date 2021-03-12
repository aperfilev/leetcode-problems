from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
                    return result

        return []

print(Solution().twoSum([2, 7, 11, 15], 9)) # [0, 1]
    # Output: Because
    # nums[0] + nums[1] == 9