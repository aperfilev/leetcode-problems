from collections.abc import Set

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        b = 0
        e = 0
        chars = set()
        maxLength = 0
        while e < len(s):
            c = s[e]
            if c not in chars:
                chars.add(c)

            else:  # char c repeating
                # move b to the next to repeating char
                c2 = None
                while b < e:
                    c2 = s[b]

                    b += 1
                    if c != c2:
                        chars.remove(c2)
                    else:
                        break

            e += 1
            maxLength = max(maxLength, e - b)
            #print(s[b: e])

        return maxLength


print(Solution().lengthOfLongestSubstring("abcabcbb")) # 3
print(Solution().lengthOfLongestSubstring("dvdf")) # 3
print(Solution().lengthOfLongestSubstring("pwwkew")) # 3
print(Solution().lengthOfLongestSubstring(" ")) # 1
print(Solution().lengthOfLongestSubstring("au")) # 2

