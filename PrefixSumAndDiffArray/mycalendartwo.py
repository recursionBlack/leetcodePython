from myLeetcodeUtils import MyCalendarTwo

# 731. 我的日程安排表 II
if __name__ == "__main__":
    # 创建Solution实例
    solution = MyCalendarTwo()

    bookTime = [10, 20]
    # 测试用例1：基础案例
    print("测试用例1输出:", solution.book(bookTime[0], bookTime[1]))
    # 预期输出:true

    bookTime = [50, 60]
    # 测试用例1：基础案例
    print("测试用例1输出:", solution.book(bookTime[0], bookTime[1]))
    # 预期输出:true

    bookTime = [10, 40]
    # 测试用例1：基础案例
    print("测试用例1输出:", solution.book(bookTime[0], bookTime[1]))
    # 预期输出:true

    bookTime = [5, 15]
    # 测试用例1：基础案例
    print("测试用例1输出:", solution.book(bookTime[0], bookTime[1]))
    # 预期输出:false

    bookTime = [5, 10]
    # 测试用例1：基础案例
    print("测试用例1输出:", solution.book(bookTime[0], bookTime[1]))
    # 预期输出:true

    bookTime = [25, 55]
    # 测试用例1：基础案例
    print("测试用例1输出:", solution.book(bookTime[0], bookTime[1]))
    # 预期输出:true