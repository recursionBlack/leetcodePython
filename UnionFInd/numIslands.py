from typing import List

# 200. 岛屿数量
class Solution:
    def __init__(self):
        self.MAXSIZE = 100001
        self.father = [1] * 100001
        self.cols = 0
        self.sets = 0

    def index(self, r: int, c: int) -> int:
        return r * self.cols + c

    def build(self, n: int, m: int, grid: List[List[str]]):
        self.cols = m
        # 为每个1分配一个父对象的索引
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    index = self.index(i, j)
                    self.father[index] = index
                    self.sets += 1

    def find(self, i: int) -> bool:
        if i != self.father[i]:
            self.father[i] = self.find(self.father[i])
        return self.father[i]

    def union(self, a: int, b: int, c: int, d: int):
        fx = self.find(self.index(a, b))
        fy = self.find(self.index(c, d))
        if fx != fy:
            self.father[fx] = fy
            self.sets -= 1

    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        self.build(n, m, grid)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    # 向左合并
                    if j > 0 and grid[i][j - 1] == '1':
                        self.union(i, j, i, j-1)
                    # 向上合并
                    if i > 0 and grid[i-1][j] == '1':
                        self.union(i, j, i-1, j)

        return self.sets

"""
首先，对每个1，分配一个集合，集合的索引，根据该1的位置所决定
然后，遍历所有元素，如果是1，则向左，或向上查看，是否也是1，
如果是，就将该1的父代表，与上一个合并，并将总的集合数量-1
最后，得到剩余的，不能继续合并的集合数，就是岛的数量
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # # 测试用例1：基础案例
    grid = [
        ['1', '1', '1', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0']
    ]
    print("测试用例1输入 = {}:".format(grid))
    print("测试用例1输出:", solution.numIslands(grid))
    # 预期输出:1

    solution2 = Solution()
    # 测试用例1：基础案例
    grid2 = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    print("测试用例1输入 = {}:".format(grid2))
    print("测试用例1输出:", solution2.numIslands(grid2))
    # 预期输出:3