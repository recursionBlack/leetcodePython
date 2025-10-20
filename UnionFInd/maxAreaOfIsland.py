from typing import List

# 695. 岛屿的最大面积
class UnionFind:
    __slots__ = "father", "cols", "size", "sets", "MAXAREA"

    def __init__(self, n: int):
        self.father: List[int] = list(range(n))
        self.size: List[int] = [1] * n
        self.sets = 0
        self.MAXAREA = 0

    def index(self, r: int, c: int) -> int:
        return r * self.cols + c

    def build(self, n: int, m: int, grid: List[List[str]]):
        self.cols = m
        # 为每个1分配一个父对象的索引
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    index = self.index(i, j)
                    self.father[index] = index
                    self.sets += 1
                    self.MAXAREA = 1

    def find(self, x: int) -> int:
        if self.father[x] != x:
            self.father[x] = self.find(self.father[x])
        return self.father[x]

    def union(self, a: int, b: int, c: int, d: int):
        fx = self.find(self.index(a, b))
        fy = self.find(self.index(c, d))
        if fx != fy:
            if self.size[fx] > self.size[fy]:
                self.father[fy] = fx
                self.size[fx] += self.size[fy]
                self.sets -= 1
                self.MAXAREA = max(self.MAXAREA, self.size[fx])
            else:
                self.father[fx] = fy
                self.size[fy] += self.size[fx]
                self.sets -= 1
                self.MAXAREA = max(self.MAXAREA, self.size[fy])


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        uf = UnionFind(n * m)
        uf.build(n, m, grid)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    # 向左合并
                    if j > 0 and grid[i][j - 1] == 1:
                        uf.union(i, j, i, j-1)
                    # 向上合并
                    if i > 0 and grid[i-1][j] == 1:
                        uf.union(i, j, i-1, j)

        return uf.MAXAREA


"""
和200题很像，不过200题求的是集合的数量，而本题求的是最大岛屿的面积
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # # 测试用例1：基础案例
    grid = [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]
    print("测试用例1输入 = {}:".format(grid))
    print("测试用例1输出:", solution.maxAreaOfIsland(grid))
    # 预期输出:6

    # # 测试用例1：基础案例
    grid = [[0,0,0,0,0,0,0,0]]
    print("测试用例1输入 = {}:".format(grid))
    print("测试用例1输出:", solution.maxAreaOfIsland(grid))
    # 预期输出:0

    # # 测试用例1：基础案例
    grid = [[1]]
    print("测试用例1输入 = {}:".format(grid))
    print("测试用例1输出:", solution.maxAreaOfIsland(grid))
    # 预期输出:1