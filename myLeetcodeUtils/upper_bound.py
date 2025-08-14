def upper_bound(arr, target):
    """
    手撕bisect_left函数
    from bisect import bisect_left
    :param arr:数组
    :param target:目标
    :return:数组中，第一个大于target的值的下标
    """
    left = 0
    right = len(arr) - 1  # 右边界初始化为数组最后一个元素的索引

    while left <= right:
        mid = left + (right - left) // 2  # 避免整数溢出（Python中无此问题，但保持习惯）

        if arr[mid] <= target:
            # 当前元素小于等于目标值，说明第一个大于target的位置在右侧
            left = mid + 1
        else:
            # 当前元素大于目标值，可能是候选位置，但需继续向左查找更左侧的符合条件位置
            right = mid - 1

    # 循环结束时，left即为第一个大于target的下标
    return left