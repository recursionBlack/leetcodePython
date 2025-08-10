from typing import List

# 401. 二进制手表
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:

        # 手撕bit_count
        def bitCnt(n: int):
            cnt = 0
            while n > 0:
                if n & 1:
                    cnt += 1
                n >>= 1

            return cnt

        ans = []
        #  直接遍历 每个时间有多少1
        for i in range(12):
            for j in range(60):
                if bitCnt(i) + bitCnt(j) == turnedOn:
                    sj = str(j) if j > 9 else ("0" + str(j))
                    ans.append(str(i) + ":" + sj)

        return ans

"""
难怪是简单题，有一种解法特别简单！就是这种解法，
其他的穷举的，回溯的，根本想不出来
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    turnedOn = 1
    print("测试用例1输入turnedOn = {}:".format(turnedOn))
    print("测试用例1输出:", solution.readBinaryWatch(turnedOn))
    # 预期输出: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]

    # 测试用例1：基础案例
    turnedOn = 9
    print("测试用例1输入turnedOn = {}:".format(turnedOn))
    print("测试用例1输出:", solution.readBinaryWatch(turnedOn))
    # 预期输出: []
