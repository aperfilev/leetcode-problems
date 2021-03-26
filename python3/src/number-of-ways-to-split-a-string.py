class Solution:
    def numWays(self, s: str) -> int:
        groups = [""]*3 # string splits
        counts = [0]*3 # count of 1 in each group
        count = self.recSplit(s, groups, 0, counts)
        return count

    def recSplit(self, rest, groups, activeGroup, counts):
        if len(rest) == 0:
            if len(groups[0]) == 0 or len(groups[1]) == 0 or len(groups[2]) == 0:
                return 0

            if counts[0] == counts[1] == counts[2]:
                # print(groups[0] + '|' + groups[1] + '|' + groups[2])
                return 1
            else:
                return 0

        totalCount = 0
        _groups = groups.copy()
        _counts = counts.copy()
        top = rest[0]
        if top == '1':
            _counts[activeGroup] += 1
        _groups[activeGroup] += top
        totalCount += self.recSplit(rest[1:], _groups, activeGroup, _counts)

        if activeGroup < len(groups) - 1:
            _activeGroup = activeGroup + 1
            _groups = groups.copy()
            _counts = counts.copy()
            top = rest[0]
            if top == '1':
                _counts[_activeGroup] += 1
            _groups[_activeGroup] += top
            totalCount += self.recSplit(rest[1:], _groups, _activeGroup, _counts)

        return totalCount

# print(Solution().numWays("10101")) #Output: 4
# print(Solution().numWays("0000")) #Output: 3
# print(Solution().numWays("100100010100110")) #Output: 12
print(Solution().numWays("0000000000000000000000100000000000000000000000000000001000000110000000000100000011000000001010000001000000000010000000000100001000000001000000000000001000000000010000000000000000000000000000000001010000000000000000000000000000000000110000000000000000000000000000011000000000001000000010110000000110100001000000000000100000100100000000000000100010000000010000000000000000000000000000101001000000001000000000000000000000000000000000000000000000010000000001010000000000000000000000000000001000000000000000000000010000010000000000000000000000010000000000000000000000100000000")) #Output:
