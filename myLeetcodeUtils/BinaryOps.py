from typing import List

def my_bin(n: int) -> str:
    """将整数转换为二进制字符串，格式如'0b101'"""
    if n == 0:
        return '0b0'

    # 处理负数
    sign = ''
    if n < 0:
        sign = '-'
        n = -n  # 转为正数处理

    bits = []
    while n > 0:
        # 取最低位（0或1）
        bits.append(str(n & 1))
        # 右移1位（等价于除以2，但用位运算）
        n = n >> 1

    # 收集的位是逆序的，需要反转
    bits.reverse()
    return f"{sign}0b{''.join(bits)}"


def binary_to_int(binary_str: str) -> int:
    """
    将二进制字符串转换为整数，使用位运算|，不使用幂运算
    参数: binary_str: 合法的二进制字符串，仅包含'0'和'1'
    返回: 对应的整数
    异常: ValueError: 如果输入不是有效的二进制字符串
    """
    # 验证输入是否为有效的二进制字符串
    if not isinstance(binary_str, str) or not binary_str or not all(c in '01' for c in binary_str):
        raise ValueError("输入必须是仅包含'0'和'1'的非空字符串")

    result = 0
    for char in binary_str:
        # 左移一位，相当于乘以2
        result <<= 1
        # 按位或操作，加上当前位的值（0或1）
        result |= int(char)

    return result


def bit_add(a: int, b: int) -> int:
    """使用位运算实现32位整数加法"""
    mask = 0xFFFFFFFF  # 32位掩码，确保结果在32位范围内
    a &= a
    b &= b
    while b != 0:
        # 计算无进位相加结果和进位
        tmp = (a ^ b) & mask
        b = ((a & b) << 1) & mask
        a = tmp
    # 处理负数情况（将32位无符号整数转换为有符号整数）
    return a if a <= 0x7FFFFFFF else ~(a ^ mask)


def bit_negate(x: int) -> int:
    """求一个数的相反数（补码：~x + 1）"""
    return bit_add(~x & 0xFFFFFFFF, 1)


def bit_sub(a: int, b: int) -> int:
    """使用位运算实现32位整数减法（a - b = a + (-b)）"""
    return bit_add(a, bit_negate(b))


def bit_mul(a: int, b: int) -> int:
    """使用位运算实现32位整数乘法"""
    mask = 0xFFFFFFFF
    sign = 0  # 0表示正，1表示负

    # 确定结果符号
    if (a < 0 and b > 0) or (a > 0 and b < 0):
        sign = 1
    # 转为正数计算
    if a < 0:
        a = bit_negate(a)
    if b < 0:
        b = bit_negate(b)

    result = 0
    while b != 0:
        # 如果b的最低位为1，则累加a
        if b & 1:
            result = bit_add(result, a)
        # a左移一位（相当于乘以2）
        a = (a << 1) & mask
        # b右移一位（相当于除以2）
        b = (b >> 1) & mask

    # 应用符号
    result = result & mask
    return bit_negate(result) if sign else result


def bit_div(a: int, b: int):
    """
    必须保证a和b都不是最小值
    :param a:
    :param b:
    :return: a / b
    """
    MASK = 0xFFFFFFFF
    x = a if a > 0 else bit_negate(a)
    y = b if b > 0 else bit_negate(b)
    ans = 0
    for i in range(30, -1, -1):
        if (x >> i) >= y:
            ans |= (1 << i) & MASK
            x = bit_sub(x, y << i)

    ans = ans & MASK
    res = 0
    if (a < 0) ^ (b < 0):
        res = bit_negate(ans)
    else:
        res = ans
    return res

def bit_divide(a: int, b: int):
    """
    位运算实现除法的完全体，考虑a或b可能是32位整型最小值的情况
    :param a:
    :param b:
    :return: a / b
    """
    MASK = 0xFFFFFFFF
    MAX_INT = 0x7FFFFFFF
    MIN_INT = bit_negate(0x80000000)  # 32位最小整数的无符号表示

    if a == MIN_INT and b == MIN_INT:
        return 1
    if a != MIN_INT and b != MIN_INT:
        return bit_div(a, b)
    if b == MIN_INT:
        return 0
    if b == bit_negate(1):
        return MAX_INT
    # a是整数最小，b不是整数最小，也不是-1
    absB = b if b > 0 else bit_negate(b)
    a = bit_add(a, absB)
    ans = bit_div(a, b)
    offset = 1 if b < 0 else bit_negate(1)
    return bit_add(ans, offset)

def bit_length(n: int):
    """
    计算整数的二进制表示长度（不包括符号位和前导零）
    参数: n: 整数（可以是正数、负数或零）
    返回: 表示该整数所需的最少二进制位数
    """
    # 处理0的特殊情况
    if n == 0:
        return 0

    # 处理负数：取绝对值，因为负数的二进制表示包含符号位，这里只计算数值部分的长度
    if n < 0:
        n = -n

    bit_length = 0
    # 循环右移，直到数值变为0
    while n > 0:
        bit_length += 1
        n = n >> 1  # 右移一位，相当于除以2并取整

    return bit_length


def bit_count(n):
    """
    计算整数二进制表示中1的个数（bit count）

    参数:
        n: 整数（可以是正数、负数或零）

    返回:
        二进制表示中1的个数
    """
    count = 0
    # 处理负数：在Python中负数以补码形式表示，且位数不固定
    # 这里将负数转换为等效的32位无符号整数进行计算
    if n < 0:
        n &= 0xFFFFFFFF  # 限制为32位无符号整数

    # 循环检查每一位
    while n > 0:
        # 检查最低位是否为1
        if n & 1:
            count += 1
        # 右移一位，处理下一位
        n = n >> 1

    return count

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

# 测试示例
if __name__ == "__main__":
    print(my_bin(0))  # 0b0
    print(my_bin(5))  # 0b101
    print(my_bin(-5))  # -0b101
    print(my_bin(10))  # 0b1010

    print(binary_to_int('101'))  # 5
    print(binary_to_int('-101'))  # -5
    print(binary_to_int('0b1010'))  # 10
    print(binary_to_int('0'))  # 0
