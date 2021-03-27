class Solution:

    def isAlpha(self, c):
        return c.isalpha() or c == "."

    def myAtoi(self, s: str) -> int:
        digits = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

        while len(s) > 0 and s[0] == " ":
            s = s[1:]

        if len(s) == 0:
            return 0

        isNegative = False
        if s[0] == "-":
            isNegative = True
            s = s[1:]
        elif s[0] == "+":
            isNegative = False
            s = s[1:]

        if len(s) == 0:
            return 0

        if s[0] == " ":
            return 0

        if self.isAlpha(s[0]) or s[0] in ['-', '+']:
            return 0

        value = 0
        value += int(s[0])
        for i in range(1, len(s)):
            if s[i] in digits:
                value *= 10
                value += int(s[i])
            elif s[i] in [" ", '.', '-', '+'] or s[i].isalpha():
                break

        value = value if not isNegative else -value

        if value < -2147483648:
            value = -2147483648
        elif 2147483647 < value:
            value = 2147483647

        return value



#print(Solution().myAtoi("   -42")) # -42
#print(Solution().myAtoi("   -42 4545")) # -42
#print(Solution().myAtoi("-91283472332"))
#print(Solution().myAtoi("3.14159")) #3
#print(Solution().myAtoi("+-12")) # -12
print(Solution().myAtoi("00000-42a1234")) #0


