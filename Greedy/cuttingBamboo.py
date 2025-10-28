from myLeetcodeUtils import QuicklyPower

class Solution:
    def cuttingBamboo(self, bamboo_len: int) -> int:
        n = bamboo_len
        if n == 2:
            return 1
        if n == 3:
            return 2

        """
        n = 4 -> 2 * 2
        n = 5 -> 3 * 2
        n = 6 -> 3 * 3
        n = 7 -> 3 * 2 * 2
        n = 8 -> 3 * 3 * 2
        n = 9 -> 3 * 3 * 3
        n = 10 -> 3 * 3 * 2 * 2
        。。。
        由此，可以得出如下规律：
        如果mod3 = 0
        则全分解成3的幂，就是最大的
        如果mod3 余1，
        则分解成（n - 4) 次3的幂，就是最大的
        如果mod3 余2，
        则分解成（n - 2) 次3的幂，是最大的
        规律来此纯观察，没啥通用的
        
        """
        mod = 1000000007    # 防止数据过长
        tail = 0            # 尾部
        thePower = 0        # 幂指数
        if n % 3 == 0:
            tail = 1
            thePower = n // 3
        elif n % 3 == 1:
            tail = 4
            thePower = (n - 4) // 3
        else:
            tail = 2
            thePower = (n - 2) // 3

        ans = QuicklyPower.power(3, thePower, mod) * tail % mod

        return ans

"""
本题的规律，没有普遍性，应该在题目告知，跟3的幂相关的，否则，初见的人，怎么会想到呢？
算法题真的好魔怔啊，本来应该考验学生的编程能力的，现在却成了理解题意的考察了
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # # 测试用例1：基础案例
    bamboo_len = 12
    print("测试用例1输入 = {}:".format(bamboo_len))
    print("测试用例1输出:", solution.cuttingBamboo(bamboo_len))
    # 预期输出: 81

    # # 测试用例1：基础案例
    bamboo_len = 10
    print("测试用例1输入 = {}:".format(bamboo_len))
    print("测试用例1输出:", solution.cuttingBamboo(bamboo_len))
    # 预期输出: 36