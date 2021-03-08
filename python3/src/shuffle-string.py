from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        output = [None] * len(s)
        for i in range(len(s)):
            output[indices[i]] = s[i]

        return "".join(output)


print(Solution().restoreString("codeleet", [4,5,6,7,0,2,1,3])) #"leetcode"