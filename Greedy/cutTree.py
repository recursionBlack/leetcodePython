"""
砍树（ZOJ）
一共有n棵树，每棵树都有两个信息：
该树的初始重量，和该树的每天增长重量
你每天最多只能砍一棵树，看下这棵树的收益为：
初始重量+它在被砍掉前的总增重
从第一天开始，你一共有m天可以砍树，返回m天内你获得的最大收益

这是刷题网站ZOJ上的一个题目，
本题依然是，按照某种顺序排序后，可以被01背包问题模型轻易解决
"""

"""
解题思路，肯定是先按照增长重量，从小到大的排序
然后，就成了01背包模型，对于dp[i][j],表示前j天以内，对于前i棵树，可以获得的最大收益
对于第i棵树，有两种选择，不砍，或砍，
不砍第i棵树，会使得dp[i][j]更大，即dp[i][j] = dp[i-1][j]
砍第i棵树，会使得dp[i][j]更大，即dp[i-1][j-1] + tree[i] * (j-1)
对于这两种方案，可能会一些疑惑，为啥还能不砍这颗树呢？实际的情况是，前面的树里，
有初始重量的差距大于第i棵树增长重量的情况，所有才会有选择方案1的情况
"""
from typing import List


class Solution:
    def __init__(self):
        self.dp = []

    def cutTree(self, tree: List[List[int]], m: int) -> int:
        n = len(tree)
        tree.sort(key=lambda t: t[1])
        # 初始化dp表
        self.dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                self.dp[i][j] = max(self.dp[i-1][j], self.dp[i-1][j-1] + tree[i-1][0] + tree[i-1][1] * (j-1))

        return self.dp[n][m]

"""
一道超级恐怖的题，光是贪心算法已经够难的了，居然还要牵扯上动态规划，不看左神的讲解，恐怕是做不出来的啊
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # # 测试用例1：基础案例
    tree = [[100, 20], [30, 100]]
    m = 2
    print("测试用例1输入 = {}, = {}:".format(tree, m))
    print("测试用例1输出:", solution.cutTree(tree, m))
    # 预期输出: 230

    # # 测试用例1：基础案例
    tree = [[2, 1], [10, 10], [1,1]]
    m = 2
    print("测试用例1输入 = {}, = {}:".format(tree, m))
    print("测试用例1输出:", solution.cutTree(tree, m))
    # 预期输出: 22