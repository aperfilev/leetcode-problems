from typing import List

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        output = []

        for i in range(len(nums)):
            output.insert(index[i], nums[i])

        return output


print(Solution().createTargetArray([0,1,2,3,4], [0,1,2,2,1])) #[0,4,1,3,2]