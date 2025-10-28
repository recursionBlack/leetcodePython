from typing import List
import heapq

# 1167. 连接棒材的最低费用（会员题）
"""
你有一些长度为正整数的棍子，这些长度以数组sticks的形式给出，sticks[i]是第i个棍子的长度
你可以通过支付x+y的成本，将任意两个长度为x和y的两个棍子连接成一个棍子，你必须连接所有棍子
直到只剩下一个棍子
返回以这种方式，连接所有棍子的最小成本

"""
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heap = sticks[:]
        heapq.heapify(heap)

        ans = 0
        while len(heap) > 1:
            tmp = 0
            tmp += heapq.heappop(heap)
            tmp += heapq.heappop(heap)
            ans += tmp
            heapq.heappush(heap, tmp)

        return ans

"""
解法其实就是大名鼎鼎的霍夫曼编码，连接成本越小的棍子，越早连接，连接成本最大的棍子，越晚连接
从而才能保证，连接到最后的成本最小，证明略
因为，越早被连接进棍子的，后面实际上被多次重新计算加，而越晚连接进来的棍子，被重复加的次数越少，与霍夫曼编码类似
huffman编码，即使用频率越高的数字，用越简短的编码，使用频率越低的数字，使用越复杂的编码
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # # 测试用例1：基础案例
    sticks = [1, 2,4,5,7,4]
    print("测试用例1输入 = {}:".format(sticks))
    print("测试用例1输出:", solution.connectSticks(sticks))
    # 预期输出:56

    # # 测试用例1：基础案例
    sticks = [1, 3, 9]
    print("测试用例1输入 = {}:".format(sticks))
    print("测试用例1输出:", solution.connectSticks(sticks))
    # 预期输出:17