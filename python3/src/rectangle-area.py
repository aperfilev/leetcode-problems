class Rect:
    def __init__(self, A: int, B: int, C: int, D: int):
        self.x1 = A
        self.y1 = B
        self.x2 = C
        self.y2 = D

    def getIntersectionArea(self, other) -> int:

        inner_x = [self.x1, self.x2, other.x1, other.x2]
        inner_y = [self.y1, self.y2, other.y1, other.y2]

        s_x1 = (other.x1 <= self.x1 <= other.x2)
        s_x2 = (other.x1 <= self.x2 <= other.x2)
        o_x1 = (self.x1 <= other.x1 <= self.x2)
        o_x2 = (self.x1 <= other.x2 <= self.x2)

        s_y1 = (other.y1 <= self.y1 <= other.y2)
        s_y2 = (other.y1 <= self.y2 <= other.y2)
        o_y1 = (self.y1 <= other.y1 <= self.y2)
        o_y2 = (self.y1 <= other.y2 <= self.y2)

        x_is = s_x1 or s_x2 or o_x1 or o_x2
        y_is = s_y1 or s_y2 or o_y1 or o_y2

        inner_x.sort()
        inner_y.sort()

        inner_x = inner_x[1:-1]
        inner_y = inner_y[1:-1]
        # print(inner_x)
        # print(inner_y)

        intersects = x_is and y_is
        if intersects:
            intersection = Rect(inner_x[0], inner_y[0], inner_x[1], inner_y[1])
            return intersection.area()
        else:
            return 0

    def area(self):
        return (self.x2 - self.x1) * (self.y2 - self.y1)

class Solution:

    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        r1 = Rect(A, B, C, D)
        r2 = Rect(E, F, G, H)

        areas = set()

        r1_area = r1.area()
        r2_area = r2.area()
        int_area = r1.getIntersectionArea(r2)
        areas.add(r1_area)
        areas.add(r2_area)
        areas.add(int_area)

        # print(areas)

        if r1_area == int_area:
            return r2_area

        if r2_area == int_area:
            return r1_area

        return r1_area + r2_area - int_area

print(Solution().computeArea(-3, 0, 3, 4, 0, -1, 9, 2)) #Output: 45
print(Solution().computeArea(-2, -2, 2, 2, -2, -2, 2, 2)) #Output: 16
