from typing import List
from collections import defaultdict

# 721. 账户合并
class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False
        if self.size[pa] > self.size[pb]:
            self.p[pb] = pa
            self.size[pa] += self.size[pb]
        else:
            self.p[pa] = pb
            self.size[pb] += self.size[pa]
        return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        d = {}  # 字典d的第一个元素是账户，第二个元素是i，i表示在并查集中的集合序号
        for i, (_, *emails) in enumerate(accounts):
            # *emails表示将该元素中除第一个值之外的其他值收集到emails列表中。
            for email in emails:
                if email in d:
                    uf.union(i, d[email])
                else:
                    d[email] = i

        g = defaultdict(set)
        for i, (_, *emails) in enumerate(accounts):
            root = uf.find(i)
            g[root].update(emails)

        return [[accounts[root][0]] + sorted(emails) for root, emails in g.items()]

"""
哈希表+并查集的应用，其中*emails的用法，以前没见过。
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # # 测试用例1：基础案例
    accounts = [
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["John", "johnnybravo@mail.com"],
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["Mary", "mary@mail.com"]
    ]
    print("测试用例1输入 = {}:".format(accounts))
    print("测试用例1输出:", solution.accountsMerge(accounts))
    # 预期输出:
    # [
    # ["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
    # ["John", "johnnybravo@mail.com"],
    # ["Mary", "mary@mail.com"]
    # ]

    # # 测试用例1：基础案例
    accounts = [
        ["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],
        ["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],
        ["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],
        ["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],
        ["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]
    ]
    print("测试用例1输入 = {}:".format(accounts))
    print("测试用例1输出:", solution.accountsMerge(accounts))
    # 预期输出:
    # [
    # ["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],
    # ["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],
    # ["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],
    # ["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],
    # ["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]
    # ]