class Solution:

    def climbStairs(self, n: int) -> int:

        if n == 0:
            return 0

        if n == 1:
            return 1

        if n == 2:
            return 2

        # nums = []
        # k = nums[1]
        # m = nums[2]
        k = 1
        m = 2
        val = 3
        for i in range(3, n + 1):
            val = k + m

            k = m
            m = val

        return val

print(Solution().climbStairs(4)) # 5
