import sys
from typing import List

"""
小美拿到了一个大小为
n
n的数组，她希望删除一个区间后，使得剩余所有元素的乘积末尾至少有
k
k个 0。小美想知道，一共有多少种不同的删除方案？
"""

class Solution:
    def solve2(self, nums: List[int], k: int) -> int:
        product = 1
        n = len(nums)
        ans = 0
        for num in nums:
            product *= num

        tail = 0
        product2 = product
        while product2 > 0 and product2 % 10 == 0:
            product2 = product2 // 10
            tail += 1

        # 如果全部数字相乘的尾部0的数量，都达不到k，则没有任何方案可以实现k个0
        if tail < k:
            return 0

        bbb = pow(10, k)
        maxDiv = product // bbb

        l, r = 0, 0
        ra = 1
        for r, num in enumerate(nums):
            ra *= num
            while l <= r and maxDiv % ra != 0:
                ra = ra // nums[l]
                l += 1
            if ra > 1 and maxDiv % ra == 0:
                ans += r - l + 1

        return ans

    def solve(self, nums: List[int], k: int) -> int:
        if k == 0:
            # 特殊情况：k=0时，所有非空子数组都满足（乘积尾部至少0个0）
            n = len(nums)
            return n * (n + 1) // 2

        # 预处理：计算每个数的因子2和因子5的数量
        cnt2 = []  # 每个元素的因子2数量
        cnt5 = []  # 每个元素的因子5数量
        for num in nums:
            c2, c5 = 0, 0
            # 统计因子2
            temp = num
            while temp % 2 == 0 and temp != 0:
                c2 += 1
                temp //= 2
            # 统计因子5
            temp = num
            while temp % 5 == 0 and temp != 0:
                c5 += 1
                temp //= 5
            cnt2.append(c2)
            cnt5.append(c5)

        # 计算前缀和（prefix2[i] = 前i个元素的因子2总数，prefix5同理）
        prefix2 = [0] * (len(nums) + 1)
        prefix5 = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix2[i + 1] = prefix2[i] + cnt2[i]
            prefix5[i + 1] = prefix5[i] + cnt5[i]

        # 滑动窗口：寻找所有 [l+1, r] 满足 2总数≥k 且 5总数≥k
        ans = 0
        left = 0  # 左指针（prefix的索引）
        for right in range(1, len(prefix2)):
            # 当前窗口 [left+1, right] 的因子2和5总数
            total2 = prefix2[right] - prefix2[left]
            total5 = prefix5[right] - prefix5[left]

            # 移动左指针，确保窗口满足条件时尽可能小
            while left < right:
                current2 = prefix2[right] - prefix2[left]
                current5 = prefix5[right] - prefix5[left]
                if current2 >= k and current5 >= k:
                    # 可以尝试左移，缩小窗口
                    left += 1
                else:
                    # 不满足，停止左移
                    break
            # 此时 [left, right) 是满足条件的最小左边界，所有 [l, right) 其中 l ≤ left-1 都满足
            ans += left

        return ans


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


"""
最终通过数量为9/30，即8个，第9个报错，说是第31行，触法对float类型太大了。
将第31行的/= 改为了// 则结果为21/30了，但这个测例比第9个还大，导致超时了，要输出的结果为37亿多，

看了好几篇评论区中的答案，然后按照自己想法重新写了一遍。
重点，元素均大于0，所以0的生成仅和因子2和5的个数有关，即0的个数为2和5的数量中的较小者，min(cnt2,cnt5)
对于数组中的每个数，计算其中包含2的个数和5的个数。最终，采取前缀和和滑动窗口，使得该区间内2的数量和5的数量的较小者，
加上k，小于所有数的乘积的0的个数。找出所有区间。
"""