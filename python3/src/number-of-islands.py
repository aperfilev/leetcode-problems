from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if grid is None or len(grid) == 0:
            return 0

        numIslands = 0
        for i in range(len(grid)):
            row = grid[i]

            for j in range(len(row)):

                if row[j] == "1":
                    # visit all neighbors
                    numIslands += 1
                    self.dfs_visit(grid, i, j)


        return numIslands

    def dfs_visit(self, grid: List[List[str]], i: int, j: int):
        if not (0 <= i < len(grid)) or not (0 <= j < len(grid[i])): # out of range
            return

        if grid[i][j] == "0": # sea or already visited
            return

        grid[i][j] = "0"

        self.dfs_visit(grid, i + 1, j)
        self.dfs_visit(grid, i - 1, j)
        self.dfs_visit(grid, i, j + 1)
        self.dfs_visit(grid, i, j - 1)


print(Solution().numIslands(
    [["1","1","1","1","0"],
     ["1","1","0","1","0"],
     ["1","1","0","0","0"],
     ["0","0","0","0","0"]])) # 1


print(Solution().numIslands(
    [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ])) # 3
