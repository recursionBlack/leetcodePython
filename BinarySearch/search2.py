from typing import List

# 81. 搜索旋转排序数组 II
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         def check(i: int) -> bool:
#             x = nums[i]
#             if x > nums[right]:
#                 return target > nums[right] and x >= target
#             return target > nums[right] or x >= target
#
#         left, right = -1, len(nums) - 1  # 开区间 (-1, n-1)
#         while left + 1 < right:  # 开区间不为空
#             mid = (left + right) // 2
#             if nums[mid] == nums[right]:
#                 right -= 1
#             elif check(mid):
#                 right = mid
#             else:
#                 left = mid
#         return nums[right] == target

"""
和33题完全不同的是，nums里会存在相同的元素，如果左右两端和中间相同，
则直接用原来153题的函数，会出现错误，因为最左端和最右端相等，难以判断转折点在哪？
所以要用完全不同的思路来解
做完了154题后，又可以套用33题调用153题的思路了
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 调用154题的函数，不要用153题的
        def findMin(nums: List[int]) -> [int, int]:
            left = 0
            right = len(nums) - 1
            while right > left and nums[right] == nums[left]:
                right -= 1

            trueR = right

            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] <= nums[right]:
                    right = mid
                else:
                    left = mid + 1
            return [left, trueR]

        lowest, right = findMin(nums)
        # 用目标值与最后位置的一个值进行比较，看看target落在了哪个区间里？
        # [0, lowest] or [lowest, trueR]
        left = 0
        if target == nums[right]:
            return True
        elif target > nums[right]:
            right = lowest - 1
        else:
            left = lowest

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

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