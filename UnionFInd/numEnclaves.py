from typing import List
from collections import defaultdict

# 1020. 飞地的数量
class UnionFind:
    def __init__(self, grid: List[List[int]]):
        m, n = len(grid), len(grid[0])
        self.parent = [0] * (m * n)
        self.rank = [0] * (m * n)
        # 该属性是核心解题属性
        self.onEdge = [False] * (m * n)
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v:
                    idx = i * n + j
                    self.parent[idx] = idx
                    if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                        self.onEdge[idx] = True

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, x: int, y: int) -> None:
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
            self.onEdge[x] |= self.onEdge[y]
        elif self.rank[x] < self.rank[y]:
            self.parent[x] = y
            self.onEdge[y] |= self.onEdge[x]
        else:
            self.parent[y] = x
            self.onEdge[x] |= self.onEdge[y]
            self.rank[x] += 1

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        uf = UnionFind(grid)
        m, n = len(grid), len(grid[0])
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v:
                    idx = i * n + j
                    # 向右合并
                    if j + 1 < n and grid[i][j + 1]:
                        uf.merge(idx, idx + 1)
                    # 向下合并
                    if i + 1 < m and grid[i + 1][j]:
                        uf.merge(idx, idx + n)

        res = 0
        for i in range(1, m-1):
            for j in range(1, n-1):
                if grid[i][j] and not uf.onEdge[uf.find(i * n + j)]:
                    res += 1

        return res

"""
未能解决该问题，核心原因，在于，没有添加，记录每个集合是否与边界已经联通的属性
虽然会解岛屿数量问题，但在该问题上，最终没有解出来
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # # 测试用例1：基础案例
    grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
    print("测试用例1输入 = {}:".format(grid))
    print("测试用例1输出:", solution.numEnclaves(grid))
    # 预期输出:3

    # # 测试用例1：基础案例
    grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
    print("测试用例1输入 = {}:".format(grid))
    print("测试用例1输出:", solution.numEnclaves(grid))
    # 预期输出:0