
# 367. 有效的完全平方数
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square < num:
                left = mid + 1
            elif square > num:
                right = mid - 1
            else:
                return True
        return False

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    num = 14
    print("测试用例1输入num = {}:".format(num))
    print("测试用例1输出:", solution.isPerfectSquare(num))
    # 预期输出: False