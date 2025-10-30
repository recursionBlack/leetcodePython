"""
平均值最小累加和
给定一个数组arr，长度为n，将其放到k个集合里，每个数字只能进一个集合，每个集合至少一个数字
求出各个集合的平均值，并将各个集合的平均值累加起来，
求累加和最小值
平均值向下取整
0 <= arr[i] <= 10^5
1 <= k <= n

来自真实大厂笔试，没有在线测试，对数器验证
"""
from typing import List

class Solution:
    def minAverageSum(self, arr: List[int], k: int) -> int:
        sorted(arr)
        ans = 0
        for i in range(k-1):
            ans += arr[i]

        sums = 0
        n = len(arr)
        for i in range(k, n):
            sums += arr[i]

        ave = sums // (n - k + 1)
        ans += ave

        return ans

"""
解法比较简单，但想出解法需要灵感，前k-1个数，每个最小的占一个，剩下的n-k个数，放在最后一个集合里，进行平均，
得到的解就是最小的，证明略，想出来就是能过。
"""


if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # # 测试用例1：基础案例
    arr = [4,10,15,24,26, 0,9,12,20, 5,18,22,30]
    k = 8
    print("测试用例1输入 = {}, = {}:".format(arr, k))
    print("测试用例1输出:", solution.minAverageSum(arr, k))
    # 预期输出: 103