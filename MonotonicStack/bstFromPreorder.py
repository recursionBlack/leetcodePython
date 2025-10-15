from myLeetcodeUtils import TreeNode
from typing import List, Optional

# 1008. 前序遍历构造二叉搜索树
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)

        def dfs(preorder: List[int], l: int, r: int) -> TreeNode:
            # 前两个条件是必须要加的，否则会溢出
            if l > r:
                 return None
            if l == r:
                return TreeNode(preorder[l])
            mid = l + 1
            # mid是列表中，第一个大于根节点的节点，实际上就是根节点的右侧分支
            while mid <= r and preorder[mid] < preorder[l]:
                mid += 1
            res = TreeNode(preorder[l])
            res.left = dfs(preorder, l+1, mid-1)
            res.right = dfs(preorder, mid, r)

            return res

        return dfs(preorder, 0, n-1)

"""
这个构造前序二叉树，本来用递归，或者深度优先搜索，就是最简单的，居然出现在了单调栈里，
而且也没有看到有人给出单调栈的解，只好用递归来做了。二叉树本来用递归解就是最方便的了
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    preorder = [8,5,1,7,10,12]
    print("测试用例1输入 = {}:".format(preorder))
    print("测试用例1输出:", solution.bstFromPreorder(preorder))
    # 预期输出:[8,5,10,1,7,null,12]

