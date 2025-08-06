from typing import List

# 713. 乘积小于 K 的子数组
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        ans = 0
        left, right = 0, 0
        product = 1

        while right < len(nums):
            product *= nums[right]
            right += 1
            while left < right and product >= k:
                product /= nums[left]
                left += 1
            # 该问题的难点，“以right为右边界的连续子数组的个数为right-left+1”
            # 右侧指针每次右移，增加的结果是(right - left)，而不是1个
            # 我自己写的是+= 1
            ans += (right - left)

        return ans

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    nums = [10,5,2,6]
    k = 100
    print("测试用例1输入nums = {}, k = {}:".format(nums, k))
    print("测试用例1输出:", solution.numSubarrayProductLessThanK(nums, k))
    # 预期输出: 8
