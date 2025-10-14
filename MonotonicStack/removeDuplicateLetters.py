from collections import Counter

# 316. 去除重复字母
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        left = Counter(s)  # 统计每个字母的出现次数
        ans = []  # 当作栈
        in_ans = set()
        for c in s:
            left[c] -= 1
            # 查看是否已经在ans里面了
            if c in in_ans:
                continue
            # 检查ans尾部字母和当前字符的大小，如果当前字母小
            # 且之后还有尾部字母（之后可以再加回来）
            while ans and c < ans[-1] and left[ans[-1]]:
                # 移除尾部字母，并在in_ans中也清理一下
                in_ans.remove(ans.pop())
            ans.append(c)
            in_ans.add(c)
        # 列表转为字符串
        return ''.join(ans)


if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    arr = "bcabc"
    print("测试用例1输入 = {}:".format(arr))
    print("测试用例1输出:", solution.removeDuplicateLetters(arr))
    # 预期输出:"abc"

    # 测试用例2：基础案例
    arr = "cbacdcbc"
    print("测试用例2输入 = {}:".format(arr))
    print("测试用例2输出:", solution.removeDuplicateLetters(arr))
    # 预期输出:"acdb"