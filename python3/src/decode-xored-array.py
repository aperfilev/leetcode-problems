from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        a = [0] * (len(encoded) + 1)
        a[0] = first
        for i in range(1, len(a)):
            a[i] = encoded[i-1] ^ a[i-1]

        return a


print(Solution().decode([1,2,3], 1))