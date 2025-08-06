from typing import List

# 3477. 水果成篮 II
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        usedB = [False] * len(baskets)
        unum = 0
        for fr in fruits:
            for i, v in enumerate(baskets):
                if fr <= v and not usedB[i]:
                    usedB[i] = True
                    unum += 1
                    break

        return len(baskets) - unum

# 直接双层for循环暴力解决就行了，虽然904用的滑动窗口法

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    fruits = [4,2,5]
    baskets = [3, 5, 4]
    print("测试用例1输入fruits = {}, baskets = {}:".format(fruits, baskets))
    print("测试用例1输出:", solution.numOfUnplacedFruits(fruits, baskets))
    # 预期输出: 1