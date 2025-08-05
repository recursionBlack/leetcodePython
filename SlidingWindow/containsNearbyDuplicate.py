from typing import List

# 219. 存在重复元素 II
## 双重for循环超时了
# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#
#         for i in range(len(nums)):
#             for j in range(i + 1, min(i + k + 1, len(nums))):
#                 if nums[i] == nums[j]:
#                     return True
#
#         return False

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        se = set()
        for i, num in enumerate(nums):
            if i > k:
                se.remove(nums[i-k-1])      # 由于窗口宽度是固定的，每次加一个就删一个
            if num in se:
                return True
            se.add(nums[i])

        return False

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    nums = [1,2,3,1]
    k = 3
    print("测试用例1输入nums = {}, k = {}:".format(nums, k))
    print("测试用例1输出:", solution.containsNearbyDuplicate(nums, k))
    # 预期输出: True

    # 测试用例2：基础案例
    nums = [99,99]
    k = 2
    print("测试用例1输入nums = {}, k = {}:".format(nums, k))
    print("测试用例1输出:", solution.containsNearbyDuplicate(nums, k))
    # 预期输出: True