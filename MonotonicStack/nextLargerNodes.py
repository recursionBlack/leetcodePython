from typing import Optional, List
from myLeetcodeUtils import ListNode

# 1019. 链表中的下一个更大节点
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        monoStack = []
        nums = []
        n = 0
        while head:
            nums.append(head.val)
            n += 1
            head = head.next

        ans = [0] * n
        for i in range(n):
            while monoStack and nums[i] >= nums[monoStack[-1]]:
                cur = monoStack[-1]
                monoStack.pop()
                ans[cur] = i
            monoStack.append(i)

        while monoStack:
            cur = monoStack[-1]
            monoStack.pop()
            ans[cur] = -1

        # 修正阶段,把相同的值，用最后一个的下一个最大值进行替换
        for i in range(n-2, -1, -1):
            if ans[i] != -1 and nums[ans[i]] == nums[i]:
                ans[i] = ans[ans[i]]

        # 把坐标改成值
        for i in range(n):
            if ans[i] == -1:
                ans[i] = 0
                continue
            ans[i] = nums[ans[i]]

        return ans


if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    # head = [2,1,5]
    # ln = ListNode()
    # ll = ln.list_to_linked_list(head)
    # print("测试用例1输入 = {}:".format(head))
    # print("测试用例1输出:", solution.nextLargerNodes(ll))
    # # 预期输出: [5,5,0]
    #
    # # 测试用例1：基础案例
    # head = [2,7,4,3,5]
    # ln = ListNode()
    # ll = ln.list_to_linked_list(head)
    # print("测试用例1输入 = {}:".format(head))
    # print("测试用例1输出:", solution.nextLargerNodes(ll))
    # # 预期输出: [7,0,5,5,0]

    # 测试用例1：基础案例
    head = [3,3]
    ln = ListNode()
    ll = ln.list_to_linked_list(head)
    print("测试用例1输入 = {}:".format(head))
    print("测试用例1输出:", solution.nextLargerNodes(ll))
    # 预期输出: [0,0]