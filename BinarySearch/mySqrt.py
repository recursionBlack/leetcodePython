
# 69. x 的平方根
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left < right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1

        return left - 1

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    # nums = [3,24,50,79,88,150,345]
    # target = 200
    # print("测试用例1输入nums = {}, target = {}:".format(nums, target))
    # print("测试用例1输出:", solution.twoSum(nums, target))
    # # 预期输出: [3, 6]

    # 测试用例1：基础案例
    x = 8
    print("测试用例1输入x = {}:".format(x))
    print("测试用例1输出:", solution.mySqrt(x))
    # 预期输出: 2