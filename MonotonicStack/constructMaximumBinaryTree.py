from typing import List,Optional
from myLeetcodeUtils import TreeNode

# 654. 最大二叉树
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        monoStack = []

        for i in range(n):
            nodeI = TreeNode(nums[i])
            while monoStack and nums[i] > monoStack[-1].val:
                cur = monoStack[-1]
                monoStack.pop()
                nodeI.left = cur
            if not monoStack:
                monoStack.append(nodeI)
                continue
            monoStack[-1].right = nodeI
            monoStack.append(nodeI)

        ans = monoStack[0]

        return ans


if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    nums = [3,2,1,6,0,5]       # 有重复值的
    print("测试用例1输入 = {}:".format(nums))
    showRes = TreeNode.level_order_with_null(solution.constructMaximumBinaryTree(nums))
    print("测试用例1输出:", showRes)
    # 预期输出: [6,3,5,null,2,0,null,null,1]