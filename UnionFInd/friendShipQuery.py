import sys
from typing import List
from collections import defaultdict

"""
小美认为，在人际交往中，但是随着时间的流逝，朋友的关系也是会慢慢变淡的，最终朋友关系就淡忘了。
现在初始有一些朋友关系，存在一些事件会导致两个人淡忘了他们的朋友关系。小美想知道某一时刻中，某两人是否可以通过朋友介绍互相认识？
事件共有 2 种：
1 u v：代表编号 u 的人和编号 v 的人淡忘了他们的朋友关系。
2 u v：代表小美查询编号 u 的人和编号 v 的人是否能通过朋友介绍互相认识。

注：介绍可以有多层，比如 2 号把 1 号介绍给 3 号，然后 3 号再把 1 号介绍给 4 号，这样 1 号和 4 号就认识了。

"""
class UnionFind:
    def __init__(self, size: int):
        self.n = size
        self.father = list(range(self.n + 1))

    def find(self, x: int) -> int:
        if x != self.father[x]:
            self.father[x] = self.find(self.father[x])
        return self.father[x]

    def union(self, x: int, y: int):
        fx = self.find(x)
        fy = self.find(y)
        if fx != fy:
            self.father[fy] = fx


class Solution:
    def solve(self, num: int, shipArray: List[List[int]], opArray: List[List[int]]) -> List[bool]:
        shipDict = defaultdict(list)
        for l, r in shipArray:
            shipDict[l].append(r)
            shipDict[r].append(l)

        # 先正向进行一遍操作，用shipDict存储经过全部正向操作后的结果
        for op, l, r in opArray:
            if op == 1:
                if r in shipDict[l]:
                    shipDict[l].remove(r)
                    shipDict[r].remove(l)

        # 将经过所有正向操作的最终结果，开始使用并查集
        uf = UnionFind(num)
        for key, val in shipDict.items():
            for i in val:
                uf.union(key, i)

        # 逆序遍历所有操作
        res = []
        opNum = len(opArray)
        for i in range(opNum-1, -1, -1):
            if opArray[i][0] == 2:
                res.append(uf.find(opArray[i][1]) == uf.find(opArray[i][2]))
            elif opArray[i][0] == 1:
                uf.union(opArray[i][1], opArray[i][2])

        return res

if __name__ == "__main__":
    solution = Solution()

    """
5 3 5
1 2
2 3
4 5
1 1 5
2 1 3
2 1 4
1 1 2
2 1 3

    """

    first_line = sys.stdin.readline().strip()
    data1 = list(map(int, first_line.split()))

    shipArray = []
    for _ in range(data1[1]):
        ship_line = sys.stdin.readline().strip()
        data2 = list(map(int, ship_line.split()))
        shipArray.append(data2)

    opArray = []
    for _ in range(data1[2]):
        op_line = sys.stdin.readline().strip()
        data3 = list(map(int, op_line.split()))
        opArray.append(data3)

    res = solution.solve(data1[0], shipArray, opArray)
    l = len(res)
    for i in range(l-1, -1, -1):
        if res[i]:
            print("Yes")
        else:
            print("No")