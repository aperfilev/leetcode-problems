class Solution:
    def isValid(self, s: str) -> bool:
        aSum = 0
        bSum = 0
        cSum = 0

        for i in range(len(s)):
            if aSum != 0:
                if s[i] == '(':

                elif s[i] == ')':

            elif bSum != 0:
                if s[i] == '[':

                elif s[i] == ']':
            elif cSum != 0:
                if s[i] == '{':

                elif s[i] == '}':






print(Solution().isValid("()[]{}")) #True