from typing import List

# 238. 除自身以外数组的乘积
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prePro = [1] * (n + 1)
        for i in range(n):
            prePro[i + 1] = prePro[i] * nums[i]

        sufPro = [1] * n
        for i in range(n - 2, -1, -1):
            sufPro[i] = sufPro[i + 1] * nums[i + 1]

        answer = [1] * n
        for i in range(n):
            answer[i] = prePro[i] * sufPro[i]

        return answer

"""
该题非常有趣的，用前缀积的概念，代替了前缀和，也首次手撕了后缀和，才发现，后缀和与前缀和同样常用

"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    nums = [1,2,3,4]
    print("测试用例1输入logs = {}:".format(nums))
    print("测试用例1输出:", solution.productExceptSelf(nums))
    # 预期输出: [24,12,8,6]

    # 测试用例1：基础案例
    nums = [-1,1,0,-3,3]
    print("测试用例1输入logs = {}:".format(nums))
    print("测试用例1输出:", solution.productExceptSelf(nums))
    # 预期输出: [0,0,9,0,0]