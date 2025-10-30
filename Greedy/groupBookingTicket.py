"""
组团买票
景区里一共有m个项目，有如下两个参数：
game[i] = {Ki, Bi}, Ki, Bi一定是正数
Ki表示折扣系数, Bi表示票价，举个例子，Ki = 2，Bi = 10
如果只有一个人买票，则单张门票的价格为Bi - Ki * 1 = 8
如果有两个人买票，则单张门票的价格为Bi - Ki * 2 = 6
所以这两人游玩该项目要花，6 * 2 = 12 元
如果有5个人买票，单张票价为Bi - Ki * 5 = 0
所以这5个人的游玩价格为0元，
人数更多，都认为要花费0元，否则公园还要倒找你钱吗？
于是可以认为，如果有x个人来买票，单张门票的价格为Bi - Ki * x
x个人玩这个项目的总花费为max{x * (Bi - Ki * x), 0}
单位一共有n个人，每个人最多可以选一个项目来玩，也可以不选任何项目，由你按照上面的规则，统一花钱购票
你想知道自己最少需要准备多少钱，就能应付可能花费最多钱的情况，返回该最保险的钱数
1 <= M、N、Ki、Bi <= 10^5
来自真实大厂的笔试，没有在线测试，对数器验证
"""

class Game:
    def __init__(self, k: int, b: int):
        self.Ki = k
        self.Bi = b
        self.people = 0

    # 如果该游戏项目，再来一个人，该项目能挣多少钱？有点像递推
    def earn(self) -> int:
        # self.Bi - (self.people + 1) * self.Ki ：当前的总人数，门票原价减少了，当前的门票价格
        # self.people * self.Ki： 之前的人，因为门票价格减少了，园区该退回的钱
        return self.Bi - (self.people + 1) * self.Ki - self.people * self.Ki

    # 自定义小于函数，用来让大根堆使用，
    def __lt__(self, other):
        return self.earn() > other.earn()

from typing import List
import heapq

class Solution:
    def groupBookingTicket(self, n: int, games: List[List[int]]) -> int:
        heap = []
        for k, b in games:
            heapq.heappush(heap, Game(k, b))

        ans = 0
        # 一个个的人，依次送到当前最挣钱的项目里去
        for i in range(n):
            # 大根堆里，最上面的是最挣钱的项目
            # 如果最挣钱的项目，挣的钱都小于0了，就该结束了
            if heap[0].earn() < 0:
                break

            # 大根堆里，堆顶的是最挣钱的项目
            cur = heapq.heappop(heap)
            # 因为该项目挣到了这个人的钱，该项目已有的人数+1，将该项目重新丢回堆内
            ans += cur.earn()
            cur.people += 1
            heapq.heappush(heap, cur)

        return ans

"""
该题的很有意思，左程云老师高度称赞，乍一看，毫无思路，题意读懂都要懵逼半天，其中，核心的思路就是，
将当前的人，送到花费最多的游戏项目里去，所以，需要定义游戏类，实时记录各个项目再加一个人，会多花费多少钱，
确实是贪心的思路，将每个人，都送到当前花费最多的游戏项目里去，总的结果，一定是总花销最多的
"""