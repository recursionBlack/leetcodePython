from typing import List

# 89. 格雷编码
class Solution:
    def grayCode(self, n: int) -> List[int]:
        res, head = [0], 1
        for i in range(n):
            for j in range(len(res) - 1, -1, -1):
                res.append(head + res[j])
            head <<= 1
        return res

"""
总结规律：
[0]
[0, 1]
[00,01,11,10]
[000,001,011,010,110,111,101,100]
根据krahets的题解，
设n阶格雷码集合为G(n)，则G(n+1)阶格雷码可以通过以下三步得到：
G(n+1)阶的长度是G(n)阶的两倍，
新增加的一倍长度的序列特点是：原序列倒置过来，前面再加个1，
前面加一的操作，实际上加的是(1 << n-1)
就比如说，三阶格雷码，相比于2阶格雷码，新增的后4位，就是之前的4位倒序一下，
然后每个前面再加上100

"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    n = 2
    print("测试用例1输入n = {}:".format(n))
    print("测试用例1输出:", solution.grayCode(n))
    # 预期输出: [0,1,3,2]

    # 测试用例1：基础案例
    n = 3
    print("测试用例1输入n = {}:".format(n))
    print("测试用例1输出:", solution.grayCode(n))
    # 预期输出: [0, 1, 3, 2, 6, 7, 5, 4]