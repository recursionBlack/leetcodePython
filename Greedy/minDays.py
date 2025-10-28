from collections import defaultdict

# 1553. 吃掉 N 个橘子的最少天数
class Solution:
    def __init__(self):
        self.dp = defaultdict(set)

    def minDays(self, n: int) -> int:

        if n <= 1:
            return n
        if n in self.dp:
            return self.dp[n]

        # 两种吃橘子的方式进行比较，第一个表示，要将橘子吃到2的整数倍或3的整数倍，要用的天数
        # 1表示，当橘子的数量，达到了2的倍数，或3的倍数，用一天吃掉他。
        # 第三个参数表示，用递归的方式，求解剩余橘子吃掉的天数
        ans = min(n % 2 + 1 + self.minDays(n // 2), n % 3 + 1 + self.minDays(n // 3))
        self.dp[n] = ans

        return ans

"""
该题的时间复杂度为O(log2 n * log3 n)
"""


if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # # 测试用例1：基础案例
    n = 10
    print("测试用例1输入 = {}:".format(n))
    print("测试用例1输出:", solution.minDays(n))
    # 预期输出:4

    # # 测试用例1：基础案例
    n = 6
    print("测试用例1输入 = {}:".format(n))
    print("测试用例1输出:", solution.minDays(n))
    # 预期输出:3