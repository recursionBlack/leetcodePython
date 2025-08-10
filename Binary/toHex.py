from typing import List

# 405. 数字转换为十六进制数
class Solution:
    def toHex(self, num: int) -> str:

        if num == 0:
            return "0"

        # 返回二进制的倒序列表
        def toBit(num: int) -> List[int]:
            cnt = []
            while num > 0:
                cnt.append(num & 1)
                num >>= 1

            return cnt

        def toHexP(num) -> str:
            bl = toBit(num)
            i = 0
            HexStr = ""
            hexPar = "0123456789abcdef"
            while i < len(bl):
                # 每次取4个
                chunk = bl[i:i + 4]
                chunk.reverse()
                # 转回整型
                x = 0
                if len(chunk) == 4:
                    x = (chunk[0] << 3) + (chunk[1] << 2) + (chunk[2] << 1) + (chunk[3])
                else:
                    # 最后一个字符串长度可能达不到4
                    for j in range(len(chunk)):
                        x += (chunk[j] << (len(chunk) - 1 - j))

                HexStr = hexPar[x] + HexStr
                i += 4
            return HexStr

        if num > 0:
            return toHexP(num)
        else:
            return toHexP((1 << 32) + num)

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    num = 26
    print("测试用例1输入num = {}:".format(num))
    print("测试用例1输出:", solution.toHex(num))
    # 预期输出: "1a"

    # 测试用例1：基础案例
    num = -1
    print("测试用例1输入num = {}:".format(num))
    print("测试用例1输出:", solution.toHex(num))
    # 预期输出: "ffffffff"