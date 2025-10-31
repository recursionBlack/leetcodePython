from collections import Counter

# 2384. 最大回文数字
class Solution:
    def largestPalindromic(self, num: str) -> str:
        num_list = [int(char) for char in num]
        cnt = Counter(num_list)
        # 中间数字，由最大的奇数个的数字所决定
        midNum = 0
        # 半边的计数器
        leftSize = 0
        res = []
        for i in range(9, 0, -1):
            if cnt[i] > 0:
                # 该数字的数量是否是奇数，若是，则将midNum等于他
                if cnt[i] & 1 and midNum == 0:
                    midNum = i
                res += str(i) * (cnt[i] // 2)
                leftSize += cnt[i] // 2

        # 9 ~ 1的数字都遍历完了，
        # 如果9`1的数字的数量，都是小于2的
        if leftSize == 0:
            return str(midNum)
        # 统计0的数量
        zeroNum = cnt[0]
        res += str(0) * (zeroNum // 2)
        leftSize += zeroNum // 2
        # 0也统计完了，该补上中间和右侧了
        # 中间数的确定
        if midNum != 0:
            res += str(midNum)
        elif zeroNum & 1:
            res += str(0)
        # 补上右边的数
        for i in range(leftSize - 1, -1, -1):
            res += res[i]

        return ''.join(res)

"""
该题，需要分析的边界条件很多，都让左神分析了，先对各种数字的数量进行一个统计，
然后考虑，中间的数字该是啥？
考虑0怎么处理
怎么记录半边的数量，并在右侧对称的补全
这些细节，都需要举例，然后一一敲定，非常的繁琐，但已经算是相当简单的问题了，
起码能想到，就是步骤多一些，比哪些完全想不出来，看到题解，才知道该咋想的题，好多了

"""


if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # # 测试用例1：基础案例
    num = "444947137"
    print("测试用例1输入 = {}:".format(num))
    print("测试用例1输出:", solution.largestPalindromic(num))
    # 预期输出: "7449447"