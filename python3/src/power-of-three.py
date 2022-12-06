import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        i = 1

        while i < n:
            i *= 3

        return i == n

print(Solution().isPowerOfThree(243)) #True
print(Solution().isPowerOfThree(27)) #True
print(Solution().isPowerOfThree(9)) #True
print(Solution().isPowerOfThree(0)) #False
print(Solution().isPowerOfThree(-3)) #False


