from typing import List
from collections import defaultdict

# 886. 可能的二分法
# 交替染色法+DFS或BFS都行

# 定义出颜色数组，每个节点都有一个颜色，0表示未查找过，1表示染成蓝色，-1表示染成红色
# 当一个节点染色完成后，查看其相邻节点，如果相邻节点未染色，则对其染色，若相邻节点已经染色了
# 查看其是否与自己异色，异色则正常，同色则表示无法分成两组
class Solution1:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
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
        # 使用字典，记录下每个节点讨厌的节点
        color = [0] * n
        for a, b in dislikes:
            a, b = a - 1, b - 1
            g[a].append(b)
            g[b].append(a)

        res = True
        for i, c in enumerate(color):
            # 只要有一个不满足，整体结果就为False
            if not (c or dfs(i, 1)):
                res = False
                break  # 提前退出循环，无需继续判断
        return res


## 并查集解法
class Solution2:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # 定义查找函数
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]
        # 定义讨厌字典，key为本节点，val为讨厌的节点
        g = defaultdict(list)
        for a, b in dislikes:
            # 老是容易忘的一句
            a, b = a - 1, b - 1
            g[a].append(b)
            g[b].append(a)
        p = list(range(n))
        for i in range(n):
            for j in g[i]:
                if find(i) == find(j):
                    return False
                # 将讨厌的节点合并到同一个集合里去
                p[find(j)] = find(g[i][0])
        return True


"""
把每两个数字，想像成一条边，那么，就要求，所有边，不可以构成一个环，否则，就会导致无法分成两组的情况。

好像还不能用构成环来解，有测例不通过,

二分图的题，本身属于图论的内容，通常用交替染色法来解，不知道为啥，会有并查集的解法
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution2()

    # 测试用例1：基础案例
    n = 4
    dislikes = [[1,2],[1,3],[2,4]]
    print("测试用例1输入={}, = {}:".format(n, dislikes))
    print("测试用例1输出:", solution.possibleBipartition(n, dislikes))
    # 预期输出:true

    # 测试用例1：基础案例
    n = 5
    dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
    print("测试用例1输入={}, = {}:".format(n, dislikes))
    print("测试用例1输出:", solution.possibleBipartition(n, dislikes))
    # 预期输出:false

    # 测试用例1：基础案例
    n = 10
    dislikes = [[4,7],[4,8],[5,6],[1,6],[3,7],[2,5],
                [5,8],[1,2],[4,9],[6,10],[8,10],[3,6],
                [2,10],[9,10],[3,9],[2,3],[1,9],[4,6],
                [5,7],[3,8],[1,8],[1,7],[2,4]]
    # 1, 3, 4, 5, 10
    # 2, 6, 7, 8, 9
    print("测试用例1输入={}, = {}:".format(n, dislikes))
    print("测试用例1输出:", solution.possibleBipartition(n, dislikes))
    # 预期输出:True