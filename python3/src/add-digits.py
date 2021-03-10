class Solution:
    def addDigits(self, num: int) -> int:
        _num = num
        while _num % 10 != _num:
            _num = self._addDigits(_num)

        return _num

    def _addDigits(self, num):
        remr = num
        sum = 0
        while remr >= 1:
            digit = remr % 10
            sum += digit

            remr = int(remr / 10)

        return sum

print(Solution().addDigits(38)) # 2