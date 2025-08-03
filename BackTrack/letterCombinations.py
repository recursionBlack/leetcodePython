from typing import List

class Solution:
    board = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    def dfs(self, digits: str, pos: int, tmp: str, path: List[str]):
        # 遍历完所有数字了，则返回结果
        if pos == len(digits):
            path.append(tmp)
            return
        # 表示按到了键盘上的第几个键
        num = eval(digits[pos])

        # 遍历某个数字对应的所有字符
        for char in self.board[num]:
            tmp += char
            # 沿着该条道路选择下去，一直走到底，结果记录到res里
            self.dfs(digits, pos+1, tmp, path)
            tmp = tmp[:-1]

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        path = []
        tmp = ""

        self.dfs(digits, 0, tmp, path)
        return path

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    digits1 = "23"
    print("测试用例1输入:", digits1)
    print("测试用例1输出:", solution.letterCombinations(digits1))
    # 预期输出: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
