from typing import List

# 136. 只出现一次的数字
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num

        return ans

"""
krahets题解：
异或运算有个重要的性质，两个相同数字异或为0，即对于任意整数有 a^a =0。
因此，若将nums中所有数字执行异或运算，留下的结果则为仅出现一次的数字
"""