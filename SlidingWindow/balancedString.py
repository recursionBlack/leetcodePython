from collections import Counter

# 1234. 替换子串得到平衡字符串
class Solution:
    def balancedString(self, s: str) -> int:
        m = len(s) // 4
        cnt = Counter(s)

        # 传入的字符串直接就是平衡的，不需要任何操作
        if len(cnt) == 4 and min(cnt.values()) == m:
            return 0

        ans = float("Inf")
        left = 0
        for right, c in enumerate(s):
            cnt[c] -= 1
            while max(cnt.values()) <= m:
                ans = min(ans, right - left + 1)
                cnt[s[left]] += 1
                left += 1

        return ans

"""
又是没看明白题意，抄答案的一题啊！
看了灵茶山艾府下面的这段话，才明白这个题究竟想要干啥呢！！！

对于本题，设子串的左右端点为left和right，枚举right，
如果子串外的任意字符的出现次数都不超过m，则说明从left到right的这段子串可以是待替换子串，
用其长度right - left + 1更新答案的最小值，并向右移动left，缩小子串长度。

这个题，三个难点，1是看懂题意，2是内层的while循环，为啥要与m比较，
3是，min(ans)为啥写在了while循环内部？

"""