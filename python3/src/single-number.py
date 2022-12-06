class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        binaryMix = 0
        for i in range(len(nums)):
            binaryMix = binaryMix ^ nums[i]

        return binaryMix
