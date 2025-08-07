from typing import List

# 81. 搜索旋转排序数组 II
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def check(i: int) -> bool:
            x = nums[i]
            if x > nums[right]:
                return target > nums[right] and x >= target
            return target > nums[right] or x >= target

        left, right = -1, len(nums) - 1  # 开区间 (-1, n-1)
        while left + 1 < right:  # 开区间不为空
            mid = (left + right) // 2
            if nums[mid] == nums[right]:
                right -= 1
            elif check(mid):
                right = mid
            else:
                left = mid
        return nums[right] == target

"""
和33题完全不同的是，nums里会存在相同的元素，如果左右两端和中间相同，
则直接用原来153题的函数，会出现错误，因为最左端和最右端相等，难以判断转折点在哪？
所以要用完全不同的思路来解
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    # nums = [1,0,1,1,1]
    # target = 0
    # print("测试用例1输入nums = {}, target = {}:".format(nums, target))
    # print("测试用例1输出:", solution.search(nums, target))
    # # 预期输出: 1

    # 测试用例1：基础案例
    nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]
    target = 2
    print("测试用例1输入nums = {}, target = {}:".format(nums, target))
    print("测试用例1输出:", solution.search(nums, target))
    # 预期输出: true