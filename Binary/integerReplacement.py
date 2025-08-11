
# 397. 整数替换
# class Solution:
#     def integerReplacement(self, n: int) -> int:
#         ans = 0
#         num = n
#         while num > 1:
#             if num & 1 == 0:    # 偶数
#                 num >>= 1
#             elif (num & 0b10) == 0 or num == 3:  # mod 4 余 1 ,3 比较特殊，需要单独处理
#                 num -= 1
#             else:  # mod 4 余 3
#                 num += 1
#
#             ans += 1
#
#         return ans

"""
这是按照题意描述的做法， 其中，对mod 4 的考量，以及3的特殊处理，是难以想到的
"""

# class Solution:
#     def integerReplacement(self, n: int) -> int:
#         if n == 1:
#             return 0
#
#         if n % 2 == 0:
#             return 1 + self.integerReplacement(n >> 1)
#         else:
#             return 1 + min(self.integerReplacement(n + 1), self.integerReplacement(n - 1))

"""
暴力递归算法，理解起来比较简单，但重复计算较多
"""


from collections import defaultdict

class Solution:
    def integerReplacement(self, n: int) -> int:

        nums = defaultdict(int)
        def dfs(n: int, nums: defaultdict(int)) -> int:
            if n == 1:
                return 0
            if n in nums:
                return nums[n]
            if n % 2 == 0:
                nums[n] = 1 + dfs(n >> 1, nums)
            else:
                nums[n] = min(1 + dfs(n - 1, nums), 1 + dfs(n + 1, nums))

            return nums[n]

        return dfs(n, nums)

""" 
带字典的递归算法，记忆化搜索方式，时间大大节省了
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    n = 8
    print("测试用例1输入n = {}:".format(n))
    print("测试用例1输出:", solution.integerReplacement(n))
    # 预期输出: 3

    # 测试用例1：基础案例
    n = 7
    print("测试用例1输入n = {}:".format(n))
    print("测试用例1输出:", solution.integerReplacement(n))
    # 预期输出: 4