from typing import List

# 162. 寻找峰值
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return left

"""
这个问题比较神奇，神奇在哪里呢？神奇在数组不再是有序的了。
二分法居然也可以查看无序的数组了？？？不看题解确实很迷惑
不过还是直接举一个例子，就能想明白了
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    nums = [1,2,3,1]
    print("测试用例1输入nums = {}:".format(nums))
    print("测试用例1输出:", solution.findPeakElement(nums))
    # 预期输出: 2

    # 测试用例1：基础案例
    nums = [1,2,1,3,5,6,4]
    print("测试用例1输入nums = {}:".format(nums))
    print("测试用例1输出:", solution.findPeakElement(nums))
    # 预期输出: 1 或 5