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


def binary_to_int(bin_str: str) -> int:
    """将二进制字符串（如'101'或'-101'）转换为整数"""
    if not bin_str:
        raise ValueError("空字符串无法转换")

    # 处理符号
    sign = 1
    start = 0
    if bin_str[0] == '-':
        sign = -1
        start = 1
    # 跳过可能的'0b'前缀
    elif bin_str.startswith('0b', 0):
        start = 2

    result = 0
    for i in range(start, len(bin_str)):
        # 每次左移1位（等价于乘以2），再加上当前位的值
        result = (result << 1) | (1 if bin_str[i] == '1' else 0)

    return result * sign


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
