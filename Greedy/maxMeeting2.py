"""
能参加的最大会议数量
给你若干会议的开始时间，结束时间
你参加某个会议期间，不能参加别的会议
返回你能参加的最大会议数量
来自真实大厂笔试，没有在线测试，对数器验证

"""
from typing import List

class Solution:
    def maxMeeting2(self, meetings: List[List[int]]) -> int:
        # 根据会议结束时间排序
        sortedMeeting = sorted(meetings, key=lambda x: x[1])
        cur = -1
        ans = 0
        for begin, end in sortedMeeting:
            if cur < begin:
                cur = end
                ans += 1

        return ans


"""
该题没有在线测试，所以就不给测例了
核心解题思路，就是想到，必须按照会议结束时间排序，然后，丢弃掉，跟当前时间冲突的会议
证明略，对数器验证

需要注意的是，千万不能按照开始时间从小到大排列，也不能按照持续时间从小到大排列，
必须按照结束时间从小到大排列才是正确的
"""