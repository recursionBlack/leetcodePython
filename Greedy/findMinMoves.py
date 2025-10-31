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