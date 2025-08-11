from typing import List

# 303. 区域和检索 - 数组不可变
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums[:]
        self.prefixSum = [0] * (len(nums) + 1)
        for i in range(1, len(self.prefixSum)):
            self.prefixSum[i] = self.prefixSum[i - 1] + nums[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum[right + 1] - self.prefixSum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


# 304. 二维区域和检索 - 矩阵不可变
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m = len(matrix)
        self.n = len(matrix[0])
        # 构造空矩阵
        self.preSum = []
        for i in range(self.m + 1):
            raw = [0] * (self.n + 1)
            self.preSum.append(raw)
        # 填入前缀和的数据
        for i in range(1, self.m + 1):
            for j in range(1, self.n + 1):
                # 计算每个矩阵[0, 0, i, j]的元素和
                self.preSum[i][j] = self.preSum[i - 1][j] + self.preSum[i][j - 1] - self.preSum[i - 1][j - 1] + matrix[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.preSum[row2 + 1][col2 + 1] - self.preSum[row2 + 1][col1] - self.preSum[row1][col2 + 1] + self.preSum[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)