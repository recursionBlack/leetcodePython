from typing import List

# 436. 寻找右区间
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # 先将原始的位置追加到各项的尾部
        for i, item in enumerate(intervals):
            item.append(i)
        intervals.sort()    # 排序

        n = len(intervals)
        ans = [-1] * n
        for _, end, id in intervals:
            left = 0
            right = n - 1
            idx = -1
            # 二分查找，注意，由于题意中，要求的是，右侧区间的起始要大于当前区间的结尾
            # 所以里面的if条件是>=
            while left <= right:
                mid = (left + right) // 2
                if intervals[mid][0] >= end:
                    idx = intervals[mid][2]
                    right = mid - 1
                else:
                    left = mid + 1
            ans[id] = idx

        return ans

"""
注意该问题的边界，是严格的大于的，所以里面的if，不再是过去的哪种，可以分成三种了，只能分成两种
需要带入考虑，如果mid刚好命中了end怎么办？最后的right和left都会挪到end左侧，
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    intervals = [[3,4],[2,3],[1,2]]
    print("测试用例1输入intervals = {}:".format(intervals))
    print("测试用例1输出:", solution.findRightInterval(intervals))
    # 预期输出: [-1,0,1]