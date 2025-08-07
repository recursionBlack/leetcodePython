from typing import List

# 154. 寻找旋转排序数组中的最小值
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while right > left and nums[right] == nums[left]:
            right -= 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]

"""
相比于153题，存在重复元素，所以直接变成困难题了，
参考81相比于33题，因为重复元素，也变得很难了
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    # nums = [1,3,5]
    # print("测试用例1输入nums = {}:".format(nums))
    # print("测试用例1输出:", solution.findMin(nums))
    # # 预期输出: 1

    # 测试用例1：基础案例
    # nums = [2,2,2,0,1]
    # print("测试用例1输入nums = {}:".format(nums))
    # print("测试用例1输出:", solution.findMin(nums))
    # # 预期输出: 0

    # 测试用例1：基础案例
    nums = [1,3,3]
    print("测试用例1输入nums = {}:".format(nums))
    print("测试用例1输出:", solution.findMin(nums))
    # 预期输出: 1