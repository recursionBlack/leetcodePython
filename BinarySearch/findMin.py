from typing import List

# 153. 寻找旋转排序数组中的最小值
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]

"""
旋转排序数组类问题的前提，所以直接抄答案了
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    nums = [3,4,5,1,2]
    print("测试用例1输入nums = {}:".format(nums))
    print("测试用例1输出:", solution.findMin(nums))
    # 预期输出: 1

    # 测试用例1：基础案例
    nums = [4,5,6,7,0,1,2]
    print("测试用例1输入nums = {}:".format(nums))
    print("测试用例1输出:", solution.findMin(nums))
    # 预期输出: 0