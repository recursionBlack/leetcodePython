from collections import defaultdict

# 424. 替换后的最长重复字符
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 思路：找到一个子串，它需满足除最长连续字串外的其它字符不超过k个；返回所有这样子串中的最长一个
        # record动态记录子串s[left:right+1]中每个字符的数量
        record = defaultdict(int)
        # max_str_len记录字串中最长的连续相同字符的长度（可能中间有间隔，但间隔次数不超过k）
        record[s[0]] = max_str_len = 1
        left, right = 0, 1
        while right < len(s):
            record[s[right]] += 1
            # 看是之前的连续字符长，还是新加入的字符构成的连续字符长
            max_str_len = max(max_str_len, record[s[right]])
            # 当前子串总长为right - left + 1，如果抛开最长连续字符后的其它字符(异类)的个数超过了k个，
            # 那么左边界右移，保证滑动窗口中非最长连续字符外的其它字符(异类)不超过k个，
            # 同时被移走的字符左边界字符的数量计数减1
            while right - left + 1 - max_str_len > k:
                record[s[left]] -= 1
                left += 1
            # 只要当前子串中的异类没超过k，那么就继续增长该字串
            right += 1
        return right - left

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    s = "ABAB"
    k = 2
    print("测试用例1输入target1 = {}, k = {}:".format(s, k))
    print("测试用例1输出:", solution.characterReplacement(s, k))
    # 预期输出: 4