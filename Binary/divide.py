from myLeetcodeUtils import bit_divide

# 29. 两数相除
# class Solution:
#     def divide(self, dividend: int, divisor: int) -> int:
#         return bit_divide(dividend, divisor)
#
#

"""
第一种解法，跟着左程云，用位运算手撕了全部的加减乘除，
并根据python的特殊情况，处理了不对对32位整型进行截断的问题
但其实题目仅仅要求不可以使用乘除法，加减法还是可以用的
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1

        # 考虑被除数为最小值的情况
        if dividend == INT_MIN:
            if divisor == 1:
                return INT_MIN
            if divisor == -1:
                return INT_MAX

        # 考虑除数为最小值的情况
        if divisor == INT_MIN:
            return 1 if dividend == INT_MIN else 0
        # 考虑被除数为 0 的情况
        if dividend == 0:
            return 0

        # 一般情况，使用二分查找
        # 将所有的正数取相反数，这样就只需要考虑一种情况
        rev = False
        if dividend > 0:
            dividend = -dividend
            rev = not rev
        if divisor > 0:
            divisor = -divisor
            rev = not rev

        def bit_multiply(a: int, b: int) -> int:
            """
            使用位运算和加减法实现乘法
            :param a: 乘数
            :param b: 被乘数
            :return: 乘积
            """
            # 处理符号，确定结果的正负
            sign = -1 if (a < 0) ^ (b < 0) else 1

            # 取绝对值进行计算，简化逻辑
            a_abs = abs(a)
            b_abs = abs(b)

            result = 0

            # 遍历被乘数的每一位
            while b_abs > 0:
                # 如果当前最低位为1，则累加乘数（左移相应的位数，即乘以2^i）
                if b_abs & 1:
                    result += a_abs

                # 乘数左移一位（相当于乘以2）
                a_abs <<= 1
                # 被乘数右移一位（处理下一位）
                b_abs >>= 1

            # 应用符号并返回结果
            return sign * result

        left = 1
        right = -dividend
        ans = 0
        while left <= right:
            # 注意溢出，并且不能使用除法
            mid = left + ((right - left) >> 1)
            if bit_multiply(mid, -divisor) <= -dividend:
                ans = mid
                # 注意溢出
                if mid == INT_MAX:
                    break
                left = mid + 1
            else:
                right = mid - 1

        return -ans if rev else ans

"""
由于原题中，并没有要求不能使用加减，所以，唯一要实现的，就是乘法，用位运算手撕乘法
有了乘法，再用二分法，就能快速找到被除数了
"""


if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    # dividend = 10
    # divisor = 3
    # print("测试用例1输入dividend = {},  divisor = {}:".format(dividend,  divisor))
    # print("测试用例1输出:", solution.divide(dividend,  divisor))
    # # 预期输出: 3
    #
    # # 测试用例1：基础案例
    # dividend = 7
    # divisor = -3
    # print("测试用例1输入dividend = {},  divisor = {}:".format(dividend, divisor))
    # print("测试用例1输出:", solution.divide(dividend, divisor))
    # # 预期输出: -2
    #
    # # 测试用例1：基础案例
    # dividend = -2147483648
    # divisor = -1
    # print("测试用例1输入dividend = {},  divisor = {}:".format(dividend, divisor))
    # print("测试用例1输出:", solution.divide(dividend, divisor))
    # # 预期输出: 2147483647

    # 测试用例1：基础案例
    dividend = 1
    divisor = 1
    print("测试用例1输入dividend = {},  divisor = {}:".format(dividend, divisor))
    print("测试用例1输出:", solution.divide(dividend, divisor))
    # 预期输出: 1