from typing import List,Optional

# 685. 冗余连接 II
class UnionFind:
    __slots__ = "father"

    def __init__(self, n: int):
        self.father: List[int] = list(range(n))

    def find(self, x: int) -> int:
        if self.father[x] != x:
            self.father[x] = self.find(self.father[x])
        return self.father[x]

    def union(self, a: int, b: int) -> bool:
        fa, fb = self.find(a), self.find(b)
        if fa == fb:
            return False
        else:
            self.father[fb] = fa

        return True

"""
相比于684题，该题增加了一个有向图的限定，
"""
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        ind = [0] * n
        # 计算每个节点的入度
        for _, v in edges:
            ind[v - 1] += 1
        # 获取指向入度为2的节点的边的索引号
        dup = [i for i, (_, v) in enumerate(edges) if ind[v - 1] == 2]
        uf = UnionFind(n)
        # 如果有入度为2的节点，对于这两个边，选择去除一个，看看是否构成树，如果不构成，去除另一条边
        if dup:
            for i, (u, v) in enumerate(edges):
                if i == dup[1]:
                    continue
                if not uf.union(u - 1, v - 1):
                    return edges[dup[0]]
            return edges[dup[1]]
        # 如果没有入度为2的节点，必存在有向环，则采用类似于684的解法即可
        for i, (u, v) in enumerate(edges):
            if not uf.union(u - 1, v - 1):
                return edges[i]


"""
1.如果有入度为 2 的节点，那么一定是两条边里删一个，看删哪个可以构成树
2. 明确没有入度为 2 的情况，那么一定有有向环，找到构成环的边返回就可以了
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # # 测试用例1：基础案例
    edges = [[1,2], [1,3], [2,3]]
    print("测试用例1输入 = {}:".format(edges))
    print("测试用例1输出:", solution.findRedundantDirectedConnection(edges))
    # 预期输出:[2,3]

    # # 测试用例1：基础案例
    edges = [[1,2], [2,3], [3,4], [4, 1], [1,5]]
    print("测试用例1输入 = {}:".format(edges))
    print("测试用例1输出:", solution.findRedundantDirectedConnection(edges))
    # 预期输出:[4, 1]

    # # 测试用例1：基础案例
    edges = [[2,1],[3,1],[4,2],[1,4]]
    print("测试用例1输入 = {}:".format(edges))
    print("测试用例1输出:", solution.findRedundantDirectedConnection(edges))
    # 预期输出:[2,1]