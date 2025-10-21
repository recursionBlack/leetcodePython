from typing import List
from collections import defaultdict

# 785. 判断二分图
# 先用并查集法
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def find(i: int) -> int:
            if i != father[i]:
                father[i] = find(father[i])
            return father[i]

        g = defaultdict(list)
        for i, nears in enumerate(graph):
            for j in nears:
                g[i].append(j)
                g[j].append(i)

        n = len(graph)
        father: List[int] = list(range(n))
        for i in range(n):
            for j in g[i]:
                fi, fj = find(i), find(j)
                if fi == fj:
                    return False
                father[fj] = find(g[i][0])

        return True

class Solution2:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # 第一个参数表示节点编号，第二个参数表示要染成的颜色
        def dfs(i: int, c: int) -> bool:
            color[i] = c
            # j表示i讨厌的节点
            for j in g[i]:
                if color[j] == c:
                    return False
                if color[j] == 0 and not dfs(j, 3 - c):     # 这里染成了0，1，2三种颜色
                    return False
            return True

        g = defaultdict(list)
        n = len(graph)
        # 使用字典，记录下每个节点讨厌的节点
        color = [0] * n
        for i, nears in enumerate(graph):
            for j in nears:
                g[i].append(j)
                g[j].append(i)

        res = True
        for i, c in enumerate(color):
            # 只要有一个不满足，整体结果就为False
            if not (c or dfs(i, 1)):
                res = False
                break  # 提前退出循环，无需继续判断
        return res

"""
和886题解法一致，都是二分图，可以同时用交叉染色法，和并查集法来解
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution2()

    # 测试用例1：基础案例
    graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
    print("测试用例1输入={}:".format(graph))
    print("测试用例1输出:", solution.isBipartite(graph))
    # 预期输出:false

    # 测试用例1：基础案例
    graph = [[1,3],[0,2],[1,3],[0,2]]
    print("测试用例1输入={}:".format(graph))
    print("测试用例1输出:", solution.isBipartite(graph))
    # 预期输出:true