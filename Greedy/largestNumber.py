from typing import List
from functools import cmp_to_key

# 179. 最大数
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 将nums转化为一个迭代器，strs注意，不是字典啊
        strs = map(str, nums)
        # lambda表达式，返回一个正数，或负数，以及0，是排序函数的第二个参数的
        compareTo = lambda x, y: int(y + x) - int(x + y)
        # join函数将一个可迭代对象（通常是字符串列表）中的所有元素拼接成一个单一的字符串
        res = ''.join(sorted(strs, key=cmp_to_key(compareTo))).lstrip('0')
        return res or '0'

"""
该题虽是贪心的第一道题，但理解起来比较简单，必须明白，拼接起来的数字哪个更大，哪个放前面
主要困扰点，在于python的自定义排序函数，中的第二个参数，以及join函数，主要在于对python语法的不明白
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # # 测试用例1：基础案例
    nums = [10,2]
    print("测试用例1输入 = {}:".format(nums))
    print("测试用例1输出:", solution.largestNumber(nums))
    # 预期输出:"210"

    # # 测试用例1：基础案例
    nums = [3,30,34,5,9]
    print("测试用例1输入 = {}:".format(nums))
    print("测试用例1输出:", solution.largestNumber(nums))
    # 预期输出: "9534330"

