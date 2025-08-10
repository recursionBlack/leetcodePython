from typing import List

# 268. 丢失的数字
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i, num in enumerate(nums):
            ans ^= num
            ans ^= i

        return ans ^ n

"""
找一个全的数组，两个数组的每一个元素相异或，最后剩下的那个就是缺失的结果了
因为相同的数字，异或得0，而缺失得数字，只有一个，没人跟他异或，最后就能剩下了
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    # nums = [3,0,1]
    # print("测试用例1输入nums = {}:".format(nums))
    # print("测试用例1输出:", solution.missingNumber(nums))
    # # 预期输出: 2
    #
    # # 测试用例1：基础案例
    # nums = [0, 1]
    # print("测试用例1输入nums = {}:".format(nums))
    # print("测试用例1输出:", solution.missingNumber(nums))
    # # 预期输出: 2

    # 测试用例1：基础案例
    nums = [9,6,4,2,3,5,7,0,1]
    print("测试用例1输入nums = {}:".format(nums))
    print("测试用例1输出:", solution.missingNumber(nums))
    # 预期输出: 8
