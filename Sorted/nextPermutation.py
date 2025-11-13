from typing import List

# 31. 下一个排列
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1:
            return
        start, r, justMax = -1, 0, 0
        # 倒序遍历
        for i in range(n-1, -1, -1):
            # 防止越界
            if i+1 <= n-1:
                # 发生了降序，记录该位置
                if nums[i] < nums[i+1]:
                    start = i
                    break

        if start == -1:
            # 如果整个数组都是从大到小排好序了，则直接排序。
            nums.sort()
            return

        # 在start之后，找到刚好比start位置处值大的值，
        # 注意，刚好的意思是，如果有多个大于start位置处的值，则选择其中最小的那个
        r = start+1
        justMax = nums[start + 1]
        for i in range(start+1, n):
            if nums[i] > nums[start] and nums[i] < justMax:
                justMax = nums[i]
                r = i
        tmp = nums[start]
        nums[start] = nums[r]
        nums[r] = tmp

        # 对于l之后的位置，进行排序，从小到大, 由于不能开辟新内存，所以需要手撕一个排序算法
        half_length = n - start - 1
        # 冒泡排序：对后半段进行排序（原地修改）
        for i in range(half_length):
            # 每轮冒泡的范围：从后半段起始位置到 "后半段末尾 - 已排序的轮次"
            for j in range(start + 1, n - 1 - i):
                # 相邻元素比较，前大后小则交换
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]


"""
该题的难点在于，如何理解，下一个刚好大于当前元素的序列？
通过倒序遍历，找到第一个发生降序的位置，若l位置处发生了降序，即l位置的值，小于l+1的值，
则说明，l位置之后，选择一个比l位置大的数，与l位置交换，就会使得当前的数组，变得更大。
在l位置之后，找到一个，刚好大于l位置数的数，对l位置之后的数，进行从小到大的排序，
既是下一个大于当前序列的序列

另一个难点在于要手撕冒泡排序，因为不允许开辟新的内存，
而对于列表内部分元素排序，一般是要先切片的，但切片会导致产生新的数组，开新内存。
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # # 测试用例1：基础案例
    # nums = [1, 2, 3]
    # print("测试用例1输入 = {},:".format(nums))
    # solution.nextPermutation(nums)
    # print("测试用例1输入 = {},:".format(nums))
    # # 预期输出: [1, 3, 2]

    # # 测试用例1：基础案例
    nums = [3, 2, 1]
    print("测试用例1输入 = {},:".format(nums))
    solution.nextPermutation(nums)
    print("测试用例1输入 = {},:".format(nums))
    # 预期输出: [1, 2, 3]

    # # 测试用例1：基础案例
    nums = [1,3,2]
    print("测试用例1输入 = {},:".format(nums))
    solution.nextPermutation(nums)
    print("测试用例1输入 = {},:".format(nums))
    # 预期输出: [2, 1, 3]