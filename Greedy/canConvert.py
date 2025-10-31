"""
1153题，字符串转化（会员题）
给出两个长度相同的字符串str1和str2，请你帮忙判断字符串1能不能在0次或多次后，转为str2
每次转化时，你可以将str1中出现的所有相同的字母变成任何其他的小写英文字母
只有在字符串str1能够通过上述方式，顺利转化为字符串str2时，才能返回true

"""
from collections import Counter
from collections import defaultdict

class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        word_cnt = Counter(str2)
        if len(word_cnt) == 26:
            return False
        g = defaultdict(int)
        n = len(str1)

        for i in range(n):
            cur = str1[i]
            # 如果当前字母在字典里未存储，则存储后直接continue
            if not g[cur]:
                g[cur] = i
                continue
            # 如果当前字母在字典里已经有了，则对比str2里的当前位置和字典存储位置，
            # 字符是否相同
            if str2[g[cur]] != str2[i]:
                return False

        return True

"""
纯举例子，多观察，没有为什么，有点像高中时学的数列，根据数列找出递推公式或者数列的每个元素的表达式，
都是列举一堆例子，然后猜想一个递推式，并试图举出反例进行推翻。
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # # 测试用例1：基础案例
    str1 = "aabcc"
    str2 = "ccdee"
    print("测试用例1输入 = {},= {}:".format(str1, str2))
    print("测试用例1输出:", solution.canConvert(str1, str2))
    # 预期输出: True