from typing import List

# 581. 最短无序连续子数组
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, 0

        def is_sorted(lst):
            # 比较原列表与排序后的列表
            return lst == sorted(lst)

        if is_sorted(nums):
            return 0

        # 两次使用单调栈
        # 第一次，从左到右，找到，最后一个，小于之前最大值的，r
        monoStack = []
        for i in range(n):
            if monoStack and nums[i] < nums[monoStack[-1]]:
                r = i
            else:
                monoStack.append(i)

        # 第二次，从右到左，找到，最后一个，大于之前最小值的，l
        monoStack = []
        for i in range(n-1, -1, -1):
            if monoStack and nums[monoStack[-1]] < nums[i]:
                l = i
            else:
                monoStack.append(i)

        return 0 if r == l else r - l + 1


if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    nums = [2,6,4,8,10,9,15]
    print("测试用例1输入 = {}:".format(nums))
    print("测试用例1输出:", solution.findUnsortedSubarray(nums))
    # 预期输出:5

    # 测试用例2：基础案例
    nums = [1,3,2,2,2]
    print("测试用例1输入 = {}:".format(nums))
    print("测试用例1输出:", solution.findUnsortedSubarray(nums))
    # 预期输出:4

    # 测试用例2：基础案例
    nums = [1,2,3,3,3]
    print("测试用例1输入 = {}:".format(nums))
    print("测试用例1输出:", solution.findUnsortedSubarray(nums))
    # 预期输出:0

    # 测试用例2：基础案例
    nums = [1,3,2,3,3]
    print("测试用例1输入 = {}:".format(nums))
    print("测试用例1输出:", solution.findUnsortedSubarray(nums))
    # 预期输出:2