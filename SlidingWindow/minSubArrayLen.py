from typing import List

# 209. 长度最小的子数组
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if not nums:
            return 0

        n = len(nums)
        ans = n + 1
        # 左窗边和右窗边
        start, end = 0, 0
        total = 0
        while end < n:
            total += nums[end]
            while total >= target:
                ans = min(ans, end - start + 1)
                total -= nums[start]
                start += 1
            end += 1

        return 0 if ans == n + 1 else ans


if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    target1 = 7
    nums1 = [2,3,1,2,4,3]
    print("测试用例1输入target1 = {}, nums1 = {}:".format(target1, nums1))
    print("测试用例1输出:", solution.minSubArrayLen(target1, nums1))
    # 预期输出: 2

    # 测试用例1：基础案例
    target2 = 213
    nums2 = [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12]
    print("测试用例1输入target1 = {}, nums1 = {}:".format(target2, nums2))
    print("测试用例1输出:", solution.minSubArrayLen(target2, nums2))
    # 预期输出: 8