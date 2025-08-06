from collections import Counter

# 1156. 单字符重复子串的最大长度
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        count = Counter(text)
        res = 0
        i = 0
        while i < len(text):
            # step1: 找出当前连续的一段 [i, j)
            j = i
            while j < len(text) and text[j] == text[i]:
                j += 1

            # step2: 如果这一段长度小于该字符出现的总数，并且前面或后面有空位，则使用 cur_cnt + 1 更新答案
            cur_cnt = j - i
            if cur_cnt < count[text[i]] and (j < len(text) or i > 0):
                res = max(res, cur_cnt + 1)

            # step3: 找到这一段后面与之相隔一个不同字符的另一段 [j + 1, k)，如果不存在则 k = j + 1
            k = j + 1
            while k < len(text) and text[k] == text[i]:
                k += 1
            res = max(res, min(k - i, count[text[i]]))
            i = j
        return res

"""
这个题，纯纯体力活，难度不高，思路也不难，但哪怕是用了内置字典，都觉得好累啊
好吧，并没有我想的那么简单，我想错了，还是直接抄答案吧，累死我了
严格来说，并不能用滑动窗口来解，是双指针问题
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    # text = "ababa"
    # print("测试用例1输入text = {}:".format(text))
    # print("测试用例1输出:", solution.maxRepOpt1(text))
    # # 预期输出: 3

    # 测试用例1：基础案例
    # text = "aaabaaa"
    # print("测试用例1输入text = {}:".format(text))
    # print("测试用例1输出:", solution.maxRepOpt1(text))
    # # 预期输出: 6

    # 测试用例1：基础案例
    # text = "abcdef"
    # print("测试用例1输入text = {}:".format(text))
    # print("测试用例1输出:", solution.maxRepOpt1(text))
    # # 预期输出: 1

    # 测试用例1：基础案例
    # text = "aabbbcaa"
    # print("测试用例1输入text = {}:".format(text))
    # print("测试用例1输出:", solution.maxRepOpt1(text))
    # # 预期输出: 3

    # 测试用例1：基础案例
    text = "abbccbcaaa"
    print("测试用例1输入text = {}:".format(text))
    print("测试用例1输出:", solution.maxRepOpt1(text))
    # 预期输出: 4