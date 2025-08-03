from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums or len(nums) < 4:
            return []

        nums.sort()
        length = len(nums)
        res = []
        for i in range(length - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[length - 3] + nums[length - 2] + nums[length - 1] < target:
                continue

            for j in range(i+1, length - 2):
                if j > i+1 and nums[j] == nums[j - 1]:
                    continue
                l = j + 1
                r = length - 1
                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]
                    if total == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        # 去重
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        r -= 1
                        # 去重
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif total < target:
                        l += 1
                    else:
                        r -= 1

        return res

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    nums1 = [1, 0, -1, 0, -2, 2]
    target1 = 0
    print("测试用例1输入:", nums1)
    print("测试用例1输出:", solution.fourSum(nums1, target1))  # 预期输出: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

    # 测试用例2：基础案例
    nums2 = [2, 2, 2, 2, 2]
    target2 = 8
    print("测试用例2输入:", nums2)
    print("测试用例2输出:", solution.fourSum(nums2, target2))  # 预期输出: [[2,2,2,2]]
