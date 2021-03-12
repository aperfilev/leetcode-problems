class Solution:
    def reverse(self, x: int) -> int:
        result = 0

        _x = x

        isNegative = (x < 0)
        if isNegative:
            _x = -x

        while True:
            digits = _x % 10
            upperValue = int(_x / 10)

            result += digits

            if upperValue <= 0:
                break

            result *= 10
            _x = upperValue

        if isNegative:
            result = -result

        big2 = pow(2, 31)

        if result < -big2 or big2 - 1 < result:
            return 0
        else:
            return result

print(Solution().reverse(123)) #Output: 321
print(Solution().reverse(-123)) #Output: -321