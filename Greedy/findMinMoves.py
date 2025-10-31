from typing import List

# 517. 超级洗衣机
class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        n = len(machines)
        allClothes = sum(machines)
        # 衣服的总数量不能整除洗衣机的数量
        if allClothes % n != 0:
            return -1
        # 每台洗衣机里应该有多少衣服
        averageCloth = allClothes // n
        leftNeed = 0
        rightNeed = 0
        ans = 0
        leftSum = 0
        bottleNeck = 0

        for i in range(n):
            # 对于每台洗衣机，计算其左侧应该需要的衣服数量，和右侧应该需求的衣服数量
            leftNeed = averageCloth * i - leftSum
            rightNeed = averageCloth * (n-i-1) - (allClothes-leftSum-machines[i])
            if leftNeed >= 0 and rightNeed >= 0:
                bottleNeck = leftNeed + rightNeed
            else:
                bottleNeck = max(abs(leftNeed), abs(rightNeed))

            ans = max(ans, bottleNeck)
            leftSum += machines[i]

        return ans

"""
其实，该题最难的步骤，已经被左程云分析完了，该题最难的就是，如何把题意变成代码语言？
以每个洗衣机为分析对象，分析其左侧需要衣服，右侧需要衣服，的各种情况，如果左右两个都需要衣服，该移动几次？
如果一侧需要衣服，一侧应该给出衣服，那达到结果的状态又应该是多少？以及最终的结果，是各个相对于各个洗衣机的最大值，还是总和？
这些，都需要举一些实际的例子，进行分析和猜想。贪心算法太需要自己举一些简单的例子了。
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # # 测试用例1：基础案例
    machines = [1,0,5]
    print("测试用例1输入 = {}:".format(machines))
    print("测试用例1输出:", solution.findMinMoves(machines))
    # 预期输出: 3

    # # 测试用例1：基础案例
    machines = [0, 3, 0]
    print("测试用例1输入 = {}:".format(machines))
    print("测试用例1输出:", solution.findMinMoves(machines))
    # 预期输出: 2