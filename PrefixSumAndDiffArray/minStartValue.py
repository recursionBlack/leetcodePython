from typing import List

# 1413. 逐步求和得到正数的最小值
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        n = len(nums)
        prefixSum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefixSum[i] = prefixSum[i-1] + nums[i-1]

        minSum = 1
        for num in prefixSum:
            minSum = min(minSum, num)

        return -minSum + 1