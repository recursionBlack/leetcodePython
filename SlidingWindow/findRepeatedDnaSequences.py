from typing import List

# 187. 重复的DNA序列
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []

        usedHash = {}
        for i in range(len(s) - 10 + 1):
            substr = s[i:i+10]
            if substr in usedHash:
                usedHash[substr] += 1
            else:
                usedHash[substr] = 1

        res = []
        for key, value in usedHash.items():
            if value > 1:
                res.append(key)

        return res

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    s1 = "AAAAAAAAAAA"
    print("测试用例1输入s1 = {}:".format(s1))
    print("测试用例1输出:", solution.findRepeatedDnaSequences(s1))
    # 预期输出: ["AAAAAAAAAA"]