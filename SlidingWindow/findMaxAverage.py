from typing import List

# 643. 子数组最大平均数 I
# class Solution:
#     def findMaxAverage(self, nums: List[int], k: int) -> float:
#
#         ans = 0.0
#         for i in range(len(nums) - k + 1):
#             ans = max(ans, sum(nums[i: i+k]))
#
#         return ans / k
### 超时了,所以还是要用滑动窗口啊，每次前后各修改一个值，最后再除以k，

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = total = sum(nums[:k])

        for i in range(k, len(nums)):
            total = total - nums[i - k] + nums[i]
            ans = max(ans, total)

        return ans / k


if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    nums = [1,12,-5,-6,50,3]
    k = 4
    print("测试用例1输入nums = {}, k = {}:".format(nums, k))
    print("测试用例1输出:", solution.findMaxAverage(nums, k))
    # 预期输出: 12.75