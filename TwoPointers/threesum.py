from typing import List

# 原始暴力解法
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         anwser = []
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 for k in range(j + 1, len(nums)):
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         anwser.append(nums[i])
#                         anwser.append(nums[j])
#                         anwser.append(nums[k])
#                         sortanswer = sorted(anwser)
#                         havesame = False
#                         if res:
#                             for item in res:
#                                 if sorted(item) == sortanswer:
#                                     havesame = True
#                                     break
#                         if not havesame:
#                             res.append(anwser[:])
#                         anwser.clear()
#
#         return res

# 优化点：
# 1.先排序
# 2.采用双指针
# 3.去重
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)    # 先排序
        n = len(nums)
        res = []
        for first in range(n):
            # 去重
            if first > 0 and nums[first] == nums[first-1]:
                continue
            # 定义双指针
            left = first + 1
            right = n - 1
            # 要找的目标
            target = - nums[first]
            while left < right:
                if nums[left] + nums[right] == target:
                    res.append([nums[first], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # 去重
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1

        return res

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    nums1 = [-1, 0, 1, 2, -1, -4]
    print("测试用例1输入:", nums1)
    print("测试用例1输出:", solution.threeSum(nums1))  # 预期输出: [[-1,-1,2],[-1,0,1]]

    # 测试用例2：空数组
    nums2 = []
    print("测试用例2输入:", nums2)
    print("测试用例2输出:", solution.threeSum(nums2))  # 预期输出: []

    # 测试用例3：含0的数组
    nums3 = [0, 0, 0, 0]
    print("测试用例3输入:", nums3)
    print("测试用例3输出:", solution.threeSum(nums3))  # 预期输出: [[0,0,0]]

    # 测试用例4：无符合条件的组合
    nums4 = [1, 2, 3]
    print("测试用例4输入:", nums4)
    print("测试用例4输出:", solution.threeSum(nums4))  # 预期输出: []