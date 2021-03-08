from typing import List

class Solution:

    def runningSum(self, nums: List[int]) -> List[int]:
        output = []
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            output.append(sum)

        return output


print(Solution().runningSum([1,2,3,4])) # Output: [1,3,6,10]