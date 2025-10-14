from typing import List

# 581. 最短无序连续子数组
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, 0

        def is_sorted(lst, ascending=True):

            # 检查列表是否已排序
            # :param
            # lst: 待检查的列表（元素需支持比较操作，如int、float、str）
            # :param
            # ascending: True = 检查升序，False = 检查降序
            # :return: 已排序返回True，未排序返回False

            # 空列表或只有1个元素的列表，默认视为已排序
            if len(lst) <= 1:
                return True

            # 遍历相邻元素（索引0到n-2，避免下一个元素越界）
            for i in range(len(lst) - 1):
                current = lst[i]
                next_elem = lst[i + 1]

                # 升序检查：当前元素 > 下一个元素 → 未排序
                if ascending and current > next_elem:
                    return False
                # 降序检查：当前元素 < 下一个元素 → 未排序
                if not ascending and current < next_elem:
                    return False

            # 遍历结束无异常 → 已排序
            return True

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