class Solution:

    def lengthOfLastWord(self, s: str) -> int:
        array = s.split()
        if len(array) == 0:
            return 0

        last_word = array[-1]
        return len(last_word)

print(Solution().lengthOfLastWord("Hello world")) # 5
print(Solution().lengthOfLastWord("Hello")) # 5
print(Solution().lengthOfLastWord("")) # 0