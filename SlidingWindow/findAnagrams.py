from typing import List
from collections import Counter

# 438. 找到字符串中所有字母异位词
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        ans = []
        cnt = Counter(p)  # 统计 p 的每种字母的出现次数
        left = 0
        for right, c in enumerate(s):
            cnt[c] -= 1  # 右端点字母进入窗口
            while cnt[c] < 0:  # 字母 c 太多了
                cnt[s[left]] += 1  # 左端点字母离开窗口
                left += 1
            if right - left + 1 == len(p):  # s' 和 p 的每种字母的出现次数都相同
                ans.append(left)  # s' 左端点下标加入答案
        return ans

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    s = "cbaebabacd"
    p = "abc"
    print("测试用例1输入s = {}, p = {}:".format(s, p))
    print("测试用例1输出:", solution.findAnagrams(s, p))
    # 预期输出: [0,6]