from collections import Counter


class Solution:
    def checkRecord(self, s: str) -> bool:
        canBeRewarder = True

        c = Counter()
        for i in range(len(s)):
            c.update(s[i])

        print(c['A'])

        return canBeRewarder



print(Solution().checkRecord("PPALLP")) # True