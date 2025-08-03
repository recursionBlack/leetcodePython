from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)  # 先排序
        n = len(nums)
        anwser = float('inf')   # 设置起始值为正无穷大
        for first in range(n):
            # 去重
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # 定义双指针
            left = first + 1
            right = n - 1

            while left < right:
                sum = nums[first] + nums[left] + nums[right]
                if abs(sum - target) < abs(anwser - target):
                    anwser = sum
                if sum < target:
                    left += 1
                else:
                    right -= 1

        return anwser

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    nums1 = [-1, 2, 1, -4]
    target1 = 1
    print("测试用例1输入:", nums1)
    print("测试用例1输出:", solution.threeSumClosest(nums1, target1))  # 预期输出: 2

    # 测试用例2：基础案例
    nums2 = [0, 0, 0]
    target2 = 10000
    print("测试用例2输入:", nums2)
    print("测试用例2输出:", solution.threeSumClosest(nums2, target2))  # 预期输出: 0

    # 测试用例3：基础案例
    nums3 = [-1000, -1000, -1000]
    target3 = 10000
    print("测试用例3输入:", nums3)
    print("测试用例3输出:", solution.threeSumClosest(nums3, target3))  # 预期输出: -3000

    # 测试用例4：基础案例
    nums4 = [-84, 92, 26, 19, -7, 9, 42, -51, 8, 30, -100, -13, -38]
    target4 = 78
    print("测试用例3输入:", nums4)
    print("测试用例3输出:", solution.threeSumClosest(nums4, target4))  # 预期输出: -3000
