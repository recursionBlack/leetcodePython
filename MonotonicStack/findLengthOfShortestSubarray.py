from typing import List

# 1574. 删除最短的子数组使剩余数组有序
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        right = n - 1
        while right and arr[right - 1] <= arr[right]:
            right -= 1
        if right == 0:  # arr 已经是非递减数组
            return 0
        # 此时 arr[right-1] > arr[right]
        ans = right  # 删除 arr[:right]
        left = 0  # 枚举 left
        while left == 0 or arr[left - 1] <= arr[left]:
            while right < n and arr[right] < arr[left]:
                right += 1
            # 此时 arr[left] <= arr[right]，删除 arr[left+1:right]
            ans = min(ans, right - left - 1)
            left += 1
        return ans



"""
这一题和最短无序数组，581题findUnsortedSubarray，很像，但又不完全一样。581题，要求最短无序数组，仍然保留
所以，无序数组的上边界必须要小于右侧有序数组的最左侧元素的，这个题呢？直接把中间无序的子序列给删了，
"""


if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    arr = [1,2,3,10,4,2,3,5]
    print("测试用例1输入 = {}:".format(arr))
    print("测试用例1输出:", solution.findLengthOfShortestSubarray(arr))
    # 预期输出:3