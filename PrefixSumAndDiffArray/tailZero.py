import sys
from typing import List

"""
小美拿到了一个大小为
n
n的数组，她希望删除一个区间后，使得剩余所有元素的乘积末尾至少有
k
k个 0。小美想知道，一共有多少种不同的删除方案？
"""
class PrefixSum:
    def __init__(self, n: int, nums: List[int]):
        self.n = n
        self.preSum = [0] * (self.n + 1)
        for i in range(self.n):
            self.preSum[i+1] = self.preSum[i] + nums[i]

    def sumRange(self, l: int, r: int) -> int:
        return self.preSum[r+1] - self.preSum[l]


class Solution:
    # 对一个数字，用2或5进行分解，看看可以分解出多少个2或5
    def divideBy(self, num: int, div: int) -> int:
        cnt = 0
        while num != 0 and num % div == 0:
            num = num // div
            cnt += 1

        return cnt

    def solve(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # 统计每个元素，可以被分解成多少个2，或5
        cnt2 = []
        cnt5 = []

        for num in nums:
            cnt2.append(self.divideBy(num, 2))
            cnt5.append(self.divideBy(num, 5))

        ps2 = PrefixSum(n, cnt2)
        ps5 = PrefixSum(n, cnt5)
        total2 = ps2.preSum[n]
        total5 = ps5.preSum[n]

        # 全部乘积总共有多少个0
        tailZero = min(total2, total5)

        if tailZero < k:
            return 0

        # 开始使用滑动窗口
        left = 0
        ans = 0

        for right in range(n):
            # 计算当前窗口[left..right]的2和5总数
            current2 = ps2.sumRange(left, right)
            current5 = ps5.sumRange(left, right)

            # 核心修正：直接判断移除后是否满足条件
            remaining2 = total2 - current2
            remaining5 = total5 - current5
            remaining_zero = min(remaining2, remaining5)

            # 若当前窗口的尾部0超过允许移除的最大值，移动左指针缩小窗口
            while left <= right and remaining_zero < k:
                left += 1
                # 更新当前窗口的2和5总数（左指针右移后）
                current2 = ps2.sumRange(left, right)
                current5 = ps5.sumRange(left, right)
                remaining2 = total2 - current2
                remaining5 = total5 - current5
                remaining_zero = min(remaining2, remaining5)

            # 此时[left..right]是满足条件的最小左边界，所有[L..right]（L ∈ [left, right]）都有效
            ans += right - left + 1

        return ans

"""
哪怕已经知道了，怎么做了，还是除了问题，掉进坑里了
千万不要，根据当前末尾的总0数，和需要保留的0的个数k，来算可以移除掉的0的个数！！！
因为可以移除的0的个数，如果按照2的个数和5的个数取较小的，那对于5来说，其2的个数和5的个数，
较小的为0个，理论上，5是无法移除掉0的，但实际上，10除以5，就剩个2了，所以，不能通过移除掉的0的个数
来进行计算。
而是要通过，移除后，剩余的0的个数，小于k，来找回2和5的。
这样才不会算错。
真的是隐藏着大坑啊！！！

"""

if __name__ == "__main__":
    solution = Solution()
    """
    5 2
    2 5 3 4 20

    """

    first_line = sys.stdin.readline().strip()
    data1 = list(map(int, first_line.split()))

    second_line = sys.stdin.readline().strip()
    data2 = list(map(int, second_line.split()))

    res = solution.solve(data2[:data1[0]], data1[1])
    print(res)
