from typing import List

# 930. 和相同的二元子数组
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans, left1, left2, sum1, sum2 = 0,0,0,0,0

        for right, in_ in enumerate(nums):
            sum1 += in_
            # 计算大于goal 的个数
            while left1 <= right and sum1 > goal:
                sum1 -= nums[left1]
                left1 += 1
            sum2 += in_
            # 计算大于等于goal的个数
            while left2 <= right and sum2 >= goal:
                sum2 -= nums[left2]
                left2 += 1
            # 正难则反，二者相减，不就就得到了 == goal的个数了么？
            ans += left2 - left1

        return ans

"""
恰好型滑动窗口解法：
通常需要两个左指针，一个负责大于，一个负责大于等于，
且，两个left1 <= right和left2 <= right的条件，都是极为必要的
最后，left2 - left1就是== goal的个数。
这个差的个数，就是左端为连续的0元素的个数。
"""
