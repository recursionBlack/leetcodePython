"""
知识竞赛
最近部门需要选择两个员工，去参加一个需要合作的知识竞赛
每个员工均有一个推理能力Ai和阅读能力Bi
如果选择第i个人和第j个人去参加竞赛，
两个人在推理方面的能力X = （Ai + Aj) / 2
两个人在阅读方面的能力Y = （Bi + Bj) / 2
现在需要最大化，他们两个表现较差一方面的能力
既让min（X，Y)最大化，问这个值最大是多少？

测试连接在牛客
"""
from typing import List


class Solution:
    def knowledgeCompetition(self, nums: List[List[int]]) -> float:
        nums.sort(key=lambda row: abs(row[0]-row[1]))
        n = len(nums)
        maxA = nums[0][0]
        maxB = nums[0][1]
        ans = 0

        for i in range(1, n):
            if nums[i][0] <= nums[i][1]:
                ans = max(ans, maxA + nums[i][0])
            else:
                ans = max(ans, maxB + nums[i][1])

            maxA = max(maxA, nums[i][0])
            maxB = max(maxB, nums[i][1])

        return ans


"""
核心思路，面对贪心，这种二维数组问题，这次需要进行排序的依据，是 推理能力减阅读能力 的绝对值
为什么要这么排序？
对于一个从小到大已经拍好序的数组，对于任意人，其左侧的人两种能力的差值，都是小于他的。
对于该位置上的人，他的那个能力较弱，就从左侧，选择该能力最强的一个人进行组队，
而即使组队后，该位置人的最弱的能力，也依然是整个队伍的短板

这个比以往的贪心更麻烦，更难以想到，别的贪心，如果是二维数组，其做法，往往是，
对其中的一个维度进行排序，再对另一个维度使用堆
而该题呢？是对两个维度的绝对值差值进行排序，从小到大遍历时，将已经遍历过的，放入大根堆里。
确实是很难想像出来的。
"""