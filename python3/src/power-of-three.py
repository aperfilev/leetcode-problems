import math

class Solution:

    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        x = round(math.log(n) / math.log(3), 10)
        return x == int(x)

print(Solution().isPowerOfThree(243)) #True
print(Solution().isPowerOfThree(27)) #True
print(Solution().isPowerOfThree(9)) #True
print(Solution().isPowerOfThree(0)) #False
print(Solution().isPowerOfThree(-3)) #False


