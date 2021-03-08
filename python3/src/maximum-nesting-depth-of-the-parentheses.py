class Solution:
    def maxDepth(self, s: str) -> int:
        currentDepth = 0
        maxDepth = 0
        for i in range(len(s)):
            if s[i] == '(':
                currentDepth += 1
                maxDepth = max(maxDepth, currentDepth)
            elif s[i] == ')':
                currentDepth -= 1

        return maxDepth


print(Solution().maxDepth("(1+(2*3)+((8)/4))+1")) # Output: 3