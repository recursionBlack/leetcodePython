from typing import List

# 1124. 表现良好的最长时间段
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        ans = s = 0     # s是前缀和
        pos = {}
        for i, x in enumerate(hours):
            s += 1 if x > 8 else -1
            if s > 0:
                ans = i + 1
            elif s - 1 in pos:
                ans = max(ans, i - pos[s - 1])
            if s not in pos:
                pos[s] = i
        return ans

"""
如果 s大于0，说明从下标 0 到当前下标的这一段，满足「表现良好的时间段」，我们更新结果 ans = i + 1。
否则，如果s-1在哈希表 pos 中，记 j = pos[s-1]，说明从下标 j 到当前下标 i 的这一段，满足「表现良好的时间段」，
我们更新结果 。
• 如果 s 不在哈希表 pos 中，我们就记录 pos[s] = i。继续遍历下一个。
"""

"""
     * 简单思路：
     * 首先对于 s > 0 的时刻，直接更新 ans，
     * 对于 s <= 0 部分将 s 的变化路径想象成 " V " 形状，
     *      在 ”下坡“阶段，s一直变小，每个s都是第一次出现，s-1、s-2、根本不存在于 哈希表，不需要考虑，
     *              或者说，0到这些位置的累加和都是非正数，都是无效的
     *      在”上坡“阶段，因为开始上坡了，所以才存在「表现良好的时间段」，此时 s-1、s-2、已经存在于哈希表中
     *              哈希表记录了s-1、s-2第一次出现的位置，s-1必然在s-2更左的位置（下坡先s-1、再s-2），所以只考虑s-1
"""

"""
pos 到底是个啥啊？？？一直没看懂，哭了
[-1, -2, -3, -4 -3, -2, -1, 0]
当s走到-1的时候，[-2, -1]的下标[1,6]，就是表现良好的最长时间段
s-(s-1) = 1 就是刚好劳累时间大于轻松时间一天的时间段。
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    hours = [9,9,6,0,6,6,9]
    print("测试用例1输入 = {}:".format(hours))
    print("测试用例1输出:", solution.longestWPI(hours))
    # 预期输出: 3

    # 测试用例1：基础案例
    # hours = [9, 9, 9]
    # print("测试用例1输入 = {}:".format(hours))
    # print("测试用例1输出:", solution.longestWPI(hours))
    # # 预期输出: 3