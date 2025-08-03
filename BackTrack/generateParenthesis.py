from typing import List

class Solution:
    # 辅助函数
    # tmp:选择中的临时路径，path：全部选完的结果路径
    def dfs(self, n: int, left: int, right: int, tmp: str, path: List[str]):
        # 所有括号均被使用完毕了
        if left == n and right == n:
            path.append(tmp)
        # 还有左括号可以选择
        if left < n:
            tmp += "("
            # 做出选择后，继续递归实现
            self.dfs(n, left + 1, right, tmp, path)
            # 取消上两步的执行，因为上一步选到底后，结果已经被记录到了path里了
            tmp = tmp[:-1]
        # 还有右括号可以选择
        if right < left:
            tmp += ")"
            # 做出选择后，继续递归实现
            self.dfs(n, left, right + 1, tmp, path)
            # 取消上两步的执行，因为上一步选到底后，结果已经被记录到了path里了
            tmp = tmp[:-1]

    def generateParenthesis(self, n: int) -> List[str]:
        path = []
        tmp = ""
        self.dfs(n, 0, 0, tmp, path)

        return path

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    n = 3
    print("测试用例1输入:", n)
    print("测试用例1输出:", solution.generateParenthesis(n))  # 预期输出: ["((()))","(()())","(())()","()(())","()()()"]

