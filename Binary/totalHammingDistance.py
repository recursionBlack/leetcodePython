from typing import List

# 477. 汉明距离总和
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        # 二进制的0~30位，10的9次方小于2的30次方
        for i in range(30):
            # c = sum(((val >> i) & 1) for val in nums)
            # 这一句太浓缩了，自己再写一个
            c = 0
            for val in nums:
                # 判断val的二进制数，第i位是否为1
                if (val >> i) & 1:
                    c += 1

            # 所有数在该二进制位上的汉明距离，就是所有等于1的，乘以所有等于0的
            ans += c * (n - c)
        return ans

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    nums = [4,14,2]
    print("测试用例1输入nums = {}:".format(nums))
    print("测试用例1输出:", solution.totalHammingDistance(nums))
    # 预期输出: 6