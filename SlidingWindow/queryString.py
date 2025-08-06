

# 1016. 子串能表示从 1 到 N 数字的二进制串
class Solution:
    def queryString(self, s: str, n: int) -> bool:

        if n == 1:
            return '1' in s

        # 先找到，小于n得最大的2**x中的x的值
        bigMi = n.bit_length() - 1

        for num in range(n, 2**(bigMi - 1), -1):
            # 获取n的二进制字符串
            binary_str = bin(num)[2:]
            if binary_str not in str:
                return False

        return True

"""
有人说，可以用从n/2到n的遍历，不过不太懂原理是啥？
所以这里保守采用了2**（k-1）到2**k再到n的遍历
也没看出来哪里用滑动窗口了
"""