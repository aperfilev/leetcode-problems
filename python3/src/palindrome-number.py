class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = "".join(list(reversed(str(x))))
        return s == str(x)



print(Solution().isPalindrome(121)) #True