from typing import List

# 287. 寻找重复数
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        min_val = 1
        max_val = len(nums)

        while min_val < max_val:
            mid = (min_val + max_val) // 2
            cnt = 0
            for num in nums:
                # 计数
                cnt = sum(min_val <= num <= mid for num in nums)
                if cnt > mid - min_val + 1:     # 个数超出范围长度，即存在重复数
                    max_val = mid
                else:
                    min_val = mid + 1

        return min_val

"""
这个问题，是二分查找的原因在于，它的数组，虽然是无序的，但其值，是有序的，
所以，我们要排除，数组是无序的，这个干扰，抓到问题的本质，值是有序的
那么，我们便可以以值进行二分，分别统计小于中值的个数，是否小于中值与最小值的差，
如果大了，说明里面有重复元素，继续对该范围进行二分，直到找到重复的数
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    nums = [1,3,4,2,2]
    print("测试用例1输入nums = {}:".format(nums))
    print("测试用例1输出:", solution.findDuplicate(nums))
    # 预期输出: 2