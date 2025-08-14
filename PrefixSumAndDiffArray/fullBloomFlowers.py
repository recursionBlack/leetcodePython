from typing import List
from sortedcontainers import SortedDict
from bisect import bisect_right

# 2251. 花期内花的数目
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        cnt = SortedDict()
        for start, end in flowers:
            cnt[start] = cnt.get(start, 0) + 1
            cnt[end+1] = cnt.get(end+1, 0) - 1

        curFlowerNum = 0       # 前缀和是，当前时间的开花数
        timeChangeArr = []
        flowerChangeArr = []

        # key是开花数发生变化的时间点，val 是本次变化的数量，通常为1，
        # 累计成前缀和了，才能算是当前时间节点和开花数
        for key, val in cnt.items():
            curFlowerNum += val
            timeChangeArr.append(key)
            flowerChangeArr.append(curFlowerNum)

        ans = []
        for peo in people:
            i = bisect_right(timeChangeArr, peo)
            ans.append(flowerChangeArr[i-1])

        return ans

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    flowers = [[1,6],[3,7],[9,12],[4,13]]
    people = [2,3,7,11]
    print("测试用例1输入 = {}, = {}:".format(flowers, people))
    print("测试用例1输出:", solution.fullBloomFlowers(flowers, people))
    # 预期输出: [1,2,2,2]

    # 测试用例1：基础案例
    flowers = [[1,10],[3,3]]
    people = [3,3,2]
    print("测试用例1输入 = {}, = {}:".format(flowers, people))
    print("测试用例1输出:", solution.fullBloomFlowers(flowers, people))
    # 预期输出: [2,2,1]