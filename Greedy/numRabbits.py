from typing import List
from collections import defaultdict

# 781. 森林中的兔子
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        g = defaultdict(int)
        for i in answers:
            g[i] += 1

        ans = 0
        for key, val in g.items():
            # 同一种数量的兔子，最少可能有几种颜色？
            group = val // (key + 1)
            if val % (key + 1) != 0:
                group += 1    # 向上取整

            ans += group * (key + 1)

        return ans


if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # # 测试用例1：基础案例
    answers = [1,1,2]
    print("测试用例1输入 = {},:".format(answers))
    print("测试用例1输出:", solution.numRabbits(answers))
    # 预期输出: 5