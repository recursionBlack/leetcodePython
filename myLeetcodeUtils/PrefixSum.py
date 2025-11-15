from typing import List

# 303. 区域和检索 - 数组不可变
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums[:]
        n = len(nums)
        # 前缀和数组的实现，非常重要，必须手撕
        self.prefixSum = [0] * (n + 1)
        for i in range(1, len(self.prefixSum)):
            self.prefixSum[i] = self.prefixSum[i-1] + nums[i-1]
        # 后缀和数组的使用，非常重要，必须手撕
        self.suffixSum = [0] * n
        for i in range(n-2, -1, -1):
            self.suffixSum[i] = self.suffixSum[i+1] + nums[i+1]

    # 前缀和数组的使用
    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum[right + 1] - self.prefixSum[left]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


# 304. 二维区域和检索 - 矩阵不可变
class NumMatrix:
    """
    二维前缀和矩阵中每个元素 prefix[i][j] 的核心意义是原始矩阵左上角到 (i-1, j-1) 区域的累加和，
    它是快速计算任意子矩形和的基础，广泛应用于二维区域求和、子矩阵问题等场景。
    """

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

    # 区域求和
    # 这里需要注意的是，填写的参数，都是原矩阵的，而前缀和矩阵，要比原矩阵在行与列都要多一格，才能对的上原矩阵
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.preSum[row2 + 1][col2 + 1] - self.preSum[row2 + 1][col1] - self.preSum[row1][col2 + 1] + self.preSum[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


import random
from bisect import bisect_left
# 528. 按权重随机选择
class RandomSelect:

    def __init__(self, w: List[int]):
        n = len(w)
        self.prefix_sum = [0] * (n + 1)

        # 前缀和
        for i in range(n):
            self.prefix_sum[i+1] = self.prefix_sum[i] + w[i]
        self.prefix_sum = self.prefix_sum[1:]
        print(self.prefix_sum)


    def pickIndex(self) -> int:
        seed = random.randint(1, self.prefix_sum[-1])
        index = bisect_left(self.prefix_sum, seed)
        return index


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


from typing import List
# 497. 非重叠矩形中的随机点
class RectsRandomPoint:

    def __init__(self, rects: List[List[int]]):
        m = len(rects)
        n = len(rects[0])
        self.rects = [[0] * n] * m
        self.prefix_sum = [0] * (m+1)       # 每个矩形的面积就是其权重
        # 计算矩形的面积
        def countPointsInRect(rect: List[int])->int:
            return (rect[2] - rect[0] + 1)*(rect[3] - rect[1] + 1)

        for i in range(m):
            self.prefix_sum[i+1] = self.prefix_sum[i] + countPointsInRect(rects[i])
            self.rects[i] = rects[i][:]

        self.prefix_sum = self.prefix_sum[1:]

    def pick(self) -> List[int]:
        # 根据权重前缀和，确定选择了哪个矩形
        seed = random.randint(1, self.prefix_sum[-1])
        index = bisect_left(self.prefix_sum, seed)
        rect = self.rects[index]
        # 确定选择的矩形内的哪个点
        x = random.randint(rect[0], rect[2])
        y = random.randint(rect[1], rect[3])
        return [x, y]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()


from sortedcontainers import SortedDict
# 731. 我的日程安排表 II
class MyCalendarTwo:
    """
    畜生问题！值的范围太大了，0~10**9，根本不能自定义一个这么长的数组，
    所以直接用差分数组的想法破灭了。只能用排序好的字典，而该字典还是一个专门的包
    需要自己导入
    不算出生问题，因为很多中等题，都是要用这种解法，会这个题，差分问题基本上就都解决了

    """

    def __init__(self):
        self.cnt = SortedDict()

    def book(self, start: int, end: int) -> bool:
        self.cnt[start] = self.cnt.get(start, 0) + 1
        self.cnt[end] = self.cnt.get(end, 0) - 1
        maxBook = 0
        # 对顺序字典的值，取前缀和，
        for c in self.cnt.values():
            maxBook += c
            if maxBook > 2:
                self.cnt[start] = self.cnt.get(start, 0) - 1
                self.cnt[end] = self.cnt.get(end, 0) + 1
                return False

        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)

# 732. 我的日程安排表 III
class MyCalendarThree:
    """
    会做731题，732题稍作修改，就能用了

    """

    def __init__(self):
        self.cnt = SortedDict()

    def book(self, start: int, end: int) -> int:
        self.cnt[start] = self.cnt.get(start, 0) + 1
        self.cnt[end] = self.cnt.get(end, 0) - 1
        maxBook = 0
        ans = 0
        # 对顺序字典的值，取前缀和，
        for c in self.cnt.values():
            maxBook += c
            ans = max(ans, maxBook)

        return ans

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)


# 差分数组工具类
class Difference:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.diff = [0] * n
        self.diff[0] = nums[0]
        for i in range(1, n):
            self.diff[i] = nums[i] - nums[i-1]

    # 给区间[i, j]内的值都增加val,可以是负数.
    # 必须会手撕，解决差分问题的核心函数
    def increment(self, i: int, j: int, val: int):
        self.diff[i] += val
        if j + 1 < len(self.diff):
            self.diff[j+1] -= val

    # 根据差分数组，返回结果数组，结果数组是差分数组的前缀和数组
    def result(self):
        n = len(self.diff)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + self.diff[i]

        return prefix_sum[1:]