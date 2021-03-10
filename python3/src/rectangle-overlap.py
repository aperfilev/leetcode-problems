from typing import List


class Solution:

    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:

        rec1_x1 = rec1[0]
        rec1_x2 = rec1[2]
        rec1_y1 = rec1[1]
        rec1_y2 = rec1[3]

        rec2_x1 = rec2[0]
        rec2_x2 = rec2[2]
        rec2_y1 = rec2[1]
        rec2_y2 = rec2[3]

        x_overlap = (rec1_x1 < rec2_x1 < rec1_x2 or rec1_x1 < rec2_x2 < rec1_x2) or rec2_x1 < rec1_x1 < rec2_x2 or rec2_x1 < rec1_x2 < rec2_x2
        if rec1_x1 == rec1_x2 or rec2_x1 == rec2_x2:
            x_overlap = False

        y_overlap = (rec1_y1 < rec2_y1 < rec1_y2 or rec1_y1 < rec2_y2 < rec1_y2) or rec2_y1 < rec1_y1 < rec2_y2 or rec2_y1 < rec1_y2 < rec2_y2
        if rec1_y1 == rec1_y2 or rec2_y1 == rec2_y2:
            y_overlap = False

        return x_overlap and y_overlap


print(Solution().isRectangleOverlap([0,0,2,2], [1,1,3,3])) # True
print(Solution().isRectangleOverlap([0,0,1,1], [1,0,2,1])) # False
print(Solution().isRectangleOverlap([11,12,13,13], [17,1,17,19])) # False
print(Solution().isRectangleOverlap([-1,0,1,1], [0,-1,0,1])) # False

