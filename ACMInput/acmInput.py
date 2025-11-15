"""
该文件，主要是练习acm模式的输入的，和leetcode的不同，基本上各种笔试题都是采用了acm模式进行输入
leetcode主要采用核心代码模式输入，用户不必关心如何输入输出，仅需将核心函数写出来就行了。
但acm模式，还需要用户自己手动处理数据的传入和输出
"""
import sys
from typing import List

class Solution:
    def fixedIO(self):
        """
        固定输入，通常是单个变量，或者单行
        对于单行，其长度不定也没关系，通过回车键结束输入
        :return:
        """
        n = int(input())
        array = list(map(int, input().split()))
        print(n)
        print(array)

    def unsureArrayCountIO(self):
        """
        每次输入的是，一行数据的长度和一行数据，此为一组，但总共多少组，无法知道
        :return:
        """
        for line in sys.stdin:
            if "EOF" in line:
                break
            # 先读每组的第一个数，表示该组的数据个数
            cnt = int(line)

            # 读取下一行，作为该组的具体内容
            data_line = sys.stdin.readline().strip()
            data = list(map(int, data_line.split()))

        print("for circle end")

    def matrixIO(self) -> List[List[str]]:
        """
        输入矩阵 m x n
        先输入一行数据，表示该矩阵的大小，
        再输入矩阵的数据
            3 4
            a b c d
            e f g h
            i j k l
        :return:
        """
        # 读取第一行：m 和 n
        first_line = sys.stdin.readline().strip()
        # 处理可能的多空格分隔（如输入"3  4"）
        m, n = map(int, first_line.split())

        matrix = []
        for _ in range(m):
            # 读取一行矩阵内容
            line = sys.stdin.readline().strip()
            # 若元素用空格分隔，则按空格拆分；否则按单个字符拆分
            # （可根据题目要求选择其中一种逻辑）
            if ' ' in line:
                # 情况1：元素用空格分隔（如"a b c d"）
                row = line.split()
                # 验证列数是否正确（可选，用于调试）
                assert len(row) == n, f"第{_ + 1}行列数不符，预期{n}，实际{len(row)}"
            else:
                # 情况2：元素连续排列（如"abcd"）
                row = list(line)
                # 验证列数是否正确（可选，用于调试）
                assert len(row) == n, f"第{_ + 1}行列数不符，预期{n}，实际{len(row)}"
            matrix.append(row)

        return matrix

    def lineNumAndlineIO(self) -> List[List[int]]:
        """
        每次，先输入一个行数，然后输入若干行
            4
            1 2 3 4
            1 2 1 1
            0 2 3 6
            5 5 2 1
        :return:
        """
        # 先读取行数
        first_line = int(input())

        matrix = []
        for _ in range(first_line):
            # 读取一行矩阵内容
            # .strip()表示裁剪掉前面空格和尾部的换行符\n
            line = sys.stdin.readline().strip()
            # .split()是将line按照空格分割成一个个的字符元素，
            # map则是将字符元组映射为名为map的可迭代对象，和zip有些类似，既不是元组，也不是字典，
            # list则是将map的可迭代对象转化为列表
            data = list(map(int, line.split()))
            matrix.append(data)

        return matrix

    def zeroOneStringIO(self) ->List[List[int]]:
        """
        如果输入的矩阵，每行是01数字串，
        则先将数字串，转为字符串，再进行分割，最后填充到矩阵中
        但python中，自己的手动输入，传进来，其实已经被默默的转化为字符串了，
        但在做题过程中，实际上，其还是数字串
            2
            0101
            1011
        :return:
        """
        # 先读取行数
        first_line = int(input())

        matrix = []
        for _ in range(first_line):
            line = sys.stdin.readline().strip()
            split_digits = [int(c) for c in line]
            data = list(map(int, split_digits))
            matrix.append(data)

        return matrix

if __name__ == "__main__":
    solution = Solution()

    # solution.fixedIO()
    # solution.unsureArrayCountIO()
    # print("matrix = {}, :".format(solution.matrixIO()))
    # print("matrix = {}, :".format(solution.lineNumAndlineIO()))
    print("matrix = {}, :".format(solution.zeroOneStringIO()))