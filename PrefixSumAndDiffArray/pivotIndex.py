from typing import List

# 724. 寻找数组的中心下标
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefixSum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefixSum[i] = prefixSum[i-1] + nums[i - 1]

        prefixSum[0] = 0
        sum = prefixSum[-1]
        for i in range(len(prefixSum) - 1):
            if prefixSum[i] == sum - prefixSum[i + 1]:
                return i

        return -1

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    nums = [1, 7, 3, 6, 5, 6]
    print("测试用例1输入nums = {}:".format(nums))
    print("测试用例1输出:", solution.pivotIndex(nums))
    # 预期输出: 3