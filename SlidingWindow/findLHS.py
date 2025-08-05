from typing import List
from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:

        ans = 0
        cnt = Counter(nums)
        ll = list(cnt.keys())
        ll.sort()

        for i in range(len(ll) - 1):
            if ll[i+1] - ll[i] == 1:
                ans = max(ans, cnt[ll[i+1]] + cnt[ll[i]])

        return ans

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    nums = [1,3,2,2,5,2,3,7]
    print("测试用例1输入nums = {}, p = :".format(nums))
    print("测试用例1输出:", solution.findLHS(nums))
    # 预期输出: 5