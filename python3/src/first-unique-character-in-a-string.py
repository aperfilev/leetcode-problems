class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = {}
        for c in s:
            if c not in counter:
                counter[c] = 0
            counter[c] += 1

        for i in range(len(s)):
            c = s[i]
            if counter[c] == 1:
                return i

        return -1

print(Solution().firstUniqChar("leetcode"))
