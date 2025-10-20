from typing import List

# 684. 冗余连接
class UnionFind:
    __slots__ = "father", "size", "sets"

    def __init__(self, n: int):
        self.father: List[int] = list(range(n))
        self.size: List[int] = [1] * n
        self.sets = n

    def find(self, x: int) -> int:
        if self.father[x] != x:
            self.father[x] = self.find(self.father[x])
        return self.father[x]

    def union(self, a: int, b: int) -> bool:
        fa, fb = self.find(a), self.find(b)
        if fa == fb:
            return False
        if self.size[fa] > self.size[fb]:
            self.father[fb] = fa
            self.size[fa] += self.size[fb]
            self.sets -= 1
        else:
            self.father[fa] = fb
            self.size[fb] += self.size[fa]
            self.sets -= 1
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        for a, b in edges:
            if not uf.union(a - 1, b - 1):
                return [a, b]

"""
该题解法很简单，但理解起来比较困难，对于每次传入进来的两个数字，
如果，二者的代表数字还不相同，则合并，若二者的代表数字已经相同了，
则返回这俩数字，
第一次见到环问题的类型。哪怕已经学了并查集，并且知道这个题该用并查集，也没有想到该怎么将题意的转化

"""


if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # # 测试用例1：基础案例
    # edges = [[1,2], [1,3], [2,3]]
    # print("测试用例1输入 = {}:".format(edges))
    # print("测试用例1输出:", solution.findRedundantConnection(edges))
    # # 预期输出:[2,3]

    # # 测试用例1：基础案例
    edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
    print("测试用例1输入 = {}:".format(edges))
    print("测试用例1输出:", solution.findRedundantConnection(edges))
    # 预期输出:[1,4]