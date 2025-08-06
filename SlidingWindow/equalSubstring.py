

# 1208. 尽可能使字符串相等
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        dist = []
        # 先计算出从s到t，每个字符的距离
        for i in range(len(s)):
            d = abs(ord(s[i]) - ord(t[i]))
            dist.append(d)
        ans = 0
        left = 0
        for right, val in enumerate(dist):
            maxCost -= val
            right += 1
            while maxCost < 0:
                maxCost += dist[left]
                left += 1
            ans = max(ans, right - left)
        return ans

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    s = "abcd"
    t = "bcdf"
    maxCost = 3
    print("测试用例1输入s = {}, t = {}, maxCost = {}:".format(s, t, maxCost))
    print("测试用例1输出:", solution.equalSubstring(s, t, maxCost))
    # 预期输出: 3