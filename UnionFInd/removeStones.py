from typing import List

# 25. 移除最多的同行或同列石头
class UnionFind:
    def __init__(self, n: int):
        # self.parent = list(range(n))
        self.parent = {}
        self.cnt = 0

    def find(self, x: int) -> int:
        # 这个if很关键
        if x not in self.parent:
            self.cnt += 1
            self.parent[x] = x
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        return self.parent[x]

    def union(self, p: int, q: int):
        leader_p = self.find(p)
        leader_q = self.find(q)
        if leader_p != leader_q:
            self.parent[leader_q] = leader_p
            self.cnt -= 1

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        uf = UnionFind(n)
        for i in range(n):
            uf.union(stones[i][0] + 10001, stones[i][1])
        return n - uf.cnt

"""
这个问题很有特点，其最大的特点在于，并不知道，列数和行数，只知道石头的数量，所以
就不能像别的并查集那样，用传统的list，并提前build好father数组了，这里，采用的是
字典，并且，将father数组的构建，放置到find函数里，边查边填充
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # # 测试用例1：基础案例
    stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
    print("测试用例1输入 = {}:".format(stones))
    print("测试用例1输出:", solution.removeStones(stones))
    # 预期输出:5
