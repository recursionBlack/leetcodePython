from typing import List
from collections import Counter, defaultdict

# 904. 水果成篮
# class Solution:
#     def totalFruit(self, fruits: List[int]) -> int:
#
#         if len(fruits) < 3:
#             return len(fruits)
#
#         ans = 0
#         cnt = Counter()
#         left, right = 0, 0
#
#         while right < len(fruits):
#             cnt[fruits[right]] += 1
#             right += 1
#             while len(cnt) > 2:
#                 cnt[fruits[left]] -= 1
#                 if cnt[fruits[left]] == 0:
#                     del cnt[fruits[left]]  # 手动删除计数为0的key
#                 left += 1
#
#             ans = max(ans, sum(cnt.values()))
#
#         return ans

"""
上面是我自写的方法，速度只有5%，下面高赞题解的方法，速度83%
速度上可以优化的点：
因为使用了Counter()而不是defaultdict(int)，导致速度极慢！
而且，外层循环，用的是while，而不是for in enumerate，导致解包速度也变慢了很多
最后，sum(cnt.values())也比right - left + 1慢了很多
"""

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        cnt = defaultdict(int)
        ans = left = 0

        for right, in_ in enumerate(fruits):
            cnt[in_] += 1
            while len(cnt) > 2:
                out = fruits[left]
                cnt[out] -= 1
                if cnt[out] == 0:
                    del cnt[out]  # 手动删除计数为0的key
                left += 1

            ans = max(ans, right - left + 1)

        return ans

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    fruits = [0,1,2,2]
    print("测试用例1输入fruits = {}:".format(fruits))
    print("测试用例1输出:", solution.totalFruit(fruits))
    # 预期输出: 3