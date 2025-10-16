from typing import List
from myLeetcodeUtils import UnionFind

# 765. 情侣牵手
class Solution:
    def build(self, size: int):
        self.parent = list(range(size))
        self.size = [1] * size
        self.MAXN = 31
        self.sets = size        # 最后剩余的集合数量，

    def find(self, i: int):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x: int, y: int):
        fx = self.find(x)
        fy = self.find(y)
        if fx != fy:
            self.parent[fx] = fy
            self.sets -= 1

    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)
        self.build(n // 2)

        for i in range(0, n, 2):
            self.union(row[i] // 2, row[i + 1] // 2)

        return int(n / 2 - self.sets)

"""
如果一个集合里，有k对情侣，一定需要交换k-1次，才能将所有情侣配对好
对于self.sets，如果一个情侣编号里，两个人恰好是情侣，那就不需要交换了
如果不是情侣，则需要对该容器进行扩张，直到把所有的情侣囊括进来。
此时，就会出现，若干个集合，在每个集合里，必包含若干对情侣，对每个集合的交换次数都是k-1
那么，所有情况的交换数量，就是容器的总大小，减去集合的数量sets，这也是sets的由来。
"""


if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    row = [0,2,1,3]
    print("测试用例1输入 = {}:".format(row))
    print("测试用例1输出:", solution.minSwapsCouples(row))
    # 预期输出:1

    # 测试用例1：基础案例
    row = [3,2,0,1]
    print("测试用例1输入 = {}:".format(row))
    print("测试用例1输出:", solution.minSwapsCouples(row))
    # 预期输出:0