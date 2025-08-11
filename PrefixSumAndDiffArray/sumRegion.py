from myLeetcodeUtils import NumMatrix

if __name__ == "__main__":
    # 创建Solution实例
    solution = NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])

    # 测试用例1：基础案例
    region = [2,1,4,3]
    print("测试用例1输入region = {}:".format(region))
    print("测试用例1输出:", solution.sumRegion(region[0], region[1], region[2], region[3]))
    # 预期输出: 8

    # 测试用例1：基础案例
    region = [1,1,2,2]
    print("测试用例1输入region = {}:".format(region))
    print("测试用例1输出:", solution.sumRegion(region[0], region[1], region[2], region[3]))
    # 预期输出: 11

    # 测试用例1：基础案例
    region = [1,2,2,4]
    print("测试用例1输入region = {}:".format(region))
    print("测试用例1输出:", solution.sumRegion(region[0], region[1], region[2], region[3]))
    # 预期输出: 12