"""
给定一个数字n,将其分成k份，求其最大乘积
来自真实大厂笔试，没有在线测试，对数器验证
"""
from myLeetcodeUtils import QuicklyPower

class Solution:
    def nkMaxValue(self, n: int, k: int) -> int:
        mod = 1000000007

        m = n % k
        d = n // k
        part1 = QuicklyPower.power(d+1, m, mod)
        part2 = QuicklyPower.power(d, k - m, mod)

        return (part1 * part2) % mod

"""
相当于LCR132砍竹子的变种，但比砍竹子简单很多, 砍竹子真的太畜生了
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # # 测试用例1：基础案例
    n = 10
    k = 4
    print("测试用例1输入 = {}, = {}:".format(n, k))
    print("测试用例1输出:", solution.nkMaxValue(n, k))
    # 预期输出: 36
