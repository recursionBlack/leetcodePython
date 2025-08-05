

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occ = set()
        right = -1
        l = len(s)
        ans = 0
        for i in range(l):
            if i > 0:
                # 右指针，移不动时，移动左指针
                occ.remove(s[i-1])
            # 右指针右移，跳出循环时，说明有重复元素了，
            # 然后就右移左指针，并擦除窗口内的已有元素，直到
            # 把窗口里与右指针的下一个元素相同的元素给擦除掉了
            # 才能重新进入while循环继续右移
            while right + 1 < l and s[right+1] not in occ:
                occ.add(s[right+1])
                right += 1
            ans = max(ans, right - i + 1)

        return ans

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    s1 = "abcabcbb"
    print("测试用例1输入s1 = {}:".format(s1))
    print("测试用例1输出:", solution.lengthOfLongestSubstring(s1))
    # 预期输出: 3