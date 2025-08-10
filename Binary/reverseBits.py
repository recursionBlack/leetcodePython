

class Solution:
    def reverseBits(self, n: int) -> int:
        rever = []
        for i in range(32):
            rever.append(n & 1)
            n >>= 1

        ans = 0
        for c in rever:
            ans <<= 1
            ans |= c

        return ans

"""
需要注意的是，这里是32位整型，而不是n右移到0为止，
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    n = 43261596
    print("测试用例1输入nums = {}:".format(n))
    print("测试用例1输出:", solution.reverseBits(n))
    # 预期输出: 964176192