from typing import List

# 2449. 使数组相似的最少操作次数
class Solution:
    # 把奇数全放左边，偶数全放数组右边的函数
    def split(self, nums: List[int]) -> int:
        n = len(nums)
        oddSize = 0
        for i in range(n):
            if nums[i] & 1:
                nums[oddSize], nums[i] = nums[i], nums[oddSize]
                oddSize += 1

        return oddSize

    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        n = len(nums)
        oddSize = self.split(nums)
        self.split(target)
        numsLeft = nums[0:oddSize]
        numsRight = nums[oddSize:n]
        numsLeft.sort()
        numsRight.sort()

        targetLeft = target[0:oddSize]
        targetRight = target[oddSize:n]
        targetLeft.sort()
        targetRight.sort()

        ans = 0
        for i in range(oddSize):
            ans += abs(targetLeft[i] - numsLeft[i])

        for i in range(n-oddSize):
            ans += abs(targetRight[i] - numsRight[i])

        return ans // 4

"""
题目中，提到的，一定是有解的，则可以大大缩减我们需要考虑的情况
由于每次都是+2-2，所以不会改变数组元素的奇偶性
将数组切割成奇数组和偶数组，并按照大小排序
并逐一对元素做差，其结果一定是4的倍数，因为题意告知是有解的，

"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # # 测试用例1：基础案例
    nums = [8,12,6]
    target = [2,14,10]
    print("测试用例1输入 = {}, = {}:".format(nums, target))
    print("测试用例1输出:", solution.makeSimilar(nums, target))
    # 预期输出: 2

    # # 测试用例1：基础案例
    nums = [1,2,5]
    target = [4,1,3]
    print("测试用例1输入 = {}, = {}:".format(nums, target))
    print("测试用例1输出:", solution.makeSimilar(nums, target))
    # 预期输出: 1