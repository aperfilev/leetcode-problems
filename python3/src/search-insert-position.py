from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.searchPos(nums, 0, len(nums)-1, target)

    def searchPos(self, nums, start, end, target):
        if start == end:
            if target <= nums[start]:
                return start
            else:
                return start + 1

        if start == end - 1:
            if nums[start] <= target <= nums[end]:
                if nums[start] == target:
                    return start
                else:
                    return end

        if target <= nums[start]:
            return start
        elif nums[end] < target:
            return end + 1
        elif nums[end] == target:
            return end
        elif nums[start] <= target <= nums[end]:
            mid = int((start + end) / 2)

            if nums[start] <= target <= nums[mid]:
                pos = self.searchPos(nums, start, mid, target)
            elif nums[mid] <= target <= nums[end]:
                pos = self.searchPos(nums, mid, end, target)

            return pos



#print(Solution().searchInsert([1,3,5,6], 4)) # 2
#print(Solution().searchInsert([1,3,5,6], 7)) # 4
#print(Solution().searchInsert([1], 2)) # 2
#print(Solution().searchInsert([1], 1)) # 0
#print(Solution().searchInsert([1, 3], 1)) # 1
print(Solution().searchInsert([1, 3, 5], 5)) # 2

