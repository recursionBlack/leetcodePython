
# 402. 移掉 K 位数字
class Solution(object):
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        remain = len(num) - k
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        return ''.join(stack[:remain]).lstrip('0') or '0'

"""
该问题最大的特点，就是引入了一个k，用来提前中指掉单调栈，只有在k不为0的时候，
栈才是单调的，k为0后，栈就不再需要考虑单调性了
"""


if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    num = "1432219"
    k = 3
    print("测试用例1输入 = {}, = {}:".format(num, k))
    print("测试用例1输出:", solution.removeKdigits(num, k))
    # 预期输出:"1219"

    # 测试用例2：基础案例
    num = "10200"
    k = 1
    print("测试用例2输入 = {}, = {}:".format(num, k))
    print("测试用例2输出:", solution.removeKdigits(num, k))
    # 预期输出:"200"