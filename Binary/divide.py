from myLeetcodeUtils import bit_divide

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        return bit_divide(dividend, divisor)


if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    # dividend = 10
    # divisor = 3
    # print("测试用例1输入dividend = {},  divisor = {}:".format(dividend,  divisor))
    # print("测试用例1输出:", solution.divide(dividend,  divisor))
    # # 预期输出: 3

    # 测试用例1：基础案例
    # dividend = 7
    # divisor = -3
    # print("测试用例1输入dividend = {},  divisor = {}:".format(dividend, divisor))
    # print("测试用例1输出:", solution.divide(dividend, divisor))
    # # 预期输出: -2

    # 测试用例1：基础案例
    dividend = -2147483648
    divisor = -1
    print("测试用例1输入dividend = {},  divisor = {}:".format(dividend, divisor))
    print("测试用例1输出:", solution.divide(dividend, divisor))
    # 预期输出: 2147483647