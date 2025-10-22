from myLeetcodeUtils import ListNode
from typing import List, Optional
import heapq

# 23. 合并 K 个升序链表
ListNode.__lt__ = lambda a, b: a.val < b.val  # 让堆可以比较节点大小

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        cur = dummy = ListNode()  # 哨兵节点，作为合并后链表头节点的前一个节点
        heap: List[Optional[ListNode]] = []
        # 小根堆
        for node in lists:
            if node:
                heap.append(node)

        # 堆化
        heapq.heapify(heap)
        # 循环直到堆空，堆的大小为k条链表
        while heap:
            # 从堆中取出最小节点，因为是小根堆，pop出来的就是堆顶，最小节点
            pre = heapq.heappop(heap)
            # 如果取出的节点还有下一个节点，将其加入堆里
            if pre.next:
                heapq.heappush(heap, pre.next)

            # 把取出来的节点，加入到最终要输出的链表中来
            cur.next = pre
            cur = cur.next

        return dummy.next


if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # # 测试用例1：基础案例
    # 测试有问题，原因在于，输入时，没有将二维数组，转化为题意中的自定义链表数组。
    lists = [[1,4,5],[1,3,4],[2,6]]
    lists2 = []
    for i in lists:
        lists2.append(ListNode.list_to_linked_list(i))

    print("测试用例1输入 = {}:".format(lists))
    res = solution.mergeKLists(lists2)
    resl = []
    while res:
        resl.append(res.val)
        res = res.next
    print("测试用例1输出:", resl)
    # 预期输出:[1,1,2,3,4,4,5,6]