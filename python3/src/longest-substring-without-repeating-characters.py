class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        chars = dict()
        for i in range(len(s)):
            if s[i] not in chars:
                chars[s[i]] = i
                maxLength = max(maxLength, len(chars))
            else:
                p = chars[s[i]] + 1

                chars[s[i]] = i
                maxLength = max(maxLength, i - p + 1)

        return maxLength

    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     longest = 0
    #     if len(s) > 0:
    #         longest = 1
    #
    #     for i in range(len(s)):
    #         for j in range(i + 1, len(s)):
    #             _s = s[i:j + 1]
    #             if longest < len(_s) and not self.hasRepeatingChars(_s):
    #                 longest = len(_s)
    #
    #     return longest
    #
    # def hasRepeatingChars(self, s):
    #     chars = set()
    #     for i in range(len(s)):
    #         if s[i] in chars:
    #             return True
    #
    #         chars.add(s[i])
    #     return False


print(Solution().lengthOfLongestSubstring("abcabcbb")) # 3
print(Solution().lengthOfLongestSubstring("dvdf")) # 3
print(Solution().lengthOfLongestSubstring("pwwkew")) # 3
print(Solution().lengthOfLongestSubstring(" ")) # 1
print(Solution().lengthOfLongestSubstring("au")) # 2

