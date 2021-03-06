class Solution:
    def checkPossibility(self, nums) -> bool:
        allowedErrors = 1
        errorPos = -1
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if allowedErrors == 0:
                    return False
                else:
                    errorPos = i
                    allowedErrors -= 1
                    
        i = errorPos
        firstCond = True
        if i > 0:
            if nums[i-1] > nums[i+1]:
                firstCond = False

        secCond = True
        if i < len(nums) - 2:
            if nums[i] > nums[i+2]:
                secCond = False

        return firstCond or secCond


print(Solution().checkPossibility([3,4,2,3]))
print(Solution().checkPossibility([3,2,2,3]))
print(Solution().checkPossibility([3,2,2,3,3,2]))
# False        