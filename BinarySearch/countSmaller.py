from typing import List
from collections import Counter

# 315. 计算右侧小于当前元素的个数
# class Solution:
#     def countSmaller(self, nums: List[int]) -> List[int]:
#         cnt = Counter(nums)
#         # 升序排序
#         sortedCnt = dict(sorted(cnt.items(), key=lambda x: x[0]))
#         ans = []
#         for i, val in enumerate(nums):
#             sum = 0
#             for key, value in sortedCnt.items():
#                 if key < val:
#                     sum += value
#             ans.append(sum)
#             sortedCnt[val] -= 1
#             if sortedCnt[val] == 0:
#                 del sortedCnt[val]
#
#         return ans

"""
一个困难题，
超时了，正确解法是用树状数组，但由于这里刷题是二分法，所以就想用counter取巧，没想到居然会超时了。
后面用一下，题解的二分算法吧。
"""

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        cop = sorted(nums)
        counts = []

        for i, num in enumerate(nums):
            left = 0
            right = len(cop) - 1
            while left <= right:
                mid = (left + right) // 2
                if cop[mid] == num:
                    while mid > 0 and cop[mid] == cop[mid - 1]:
                        mid -= 1
                    counts.append(mid)
                    cop.remove(num)
                    break
                elif cop[mid] < num:
                    left = mid + 1
                else:
                    right = mid - 1

        return counts

"""
二分法时间也超时了，没办法，只能用树状数组来解了。这题就只能搁置在这了
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    nums = [5,2,6,1]
    print("测试用例1输入nums = {}:".format(nums))
    print("测试用例1输出:", solution.countSmaller(nums))
    # 预期输出: [2,1,1,0]