from collections import Counter

# 567. 字符串的排列
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        cnt = Counter(s1)  # 统计 p 的每种字母的出现次数

        for i in range(len(s2) - len(s1) + 1):
            cnt2 = Counter(s2[i:i + len(s1)])
            if cnt2 == cnt:
                return True

        return False

# 哈哈，终于做出来一道，不过好慢啊

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    s1 = "adc"
    s2 = "dcda"
    print("测试用例1输入s = {}, p = {}:".format(s1, s2))
    print("测试用例1输出:", solution.checkInclusion(s1, s2))
    # 预期输出: True
