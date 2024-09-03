class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nums = []
        for row in range(len(board)):
            for col in range(len(board)):
                num = board[row][col]
                if num!=".":
                    nums+=[(num, row), (col, num), (row//3, col//3, num)]
        unique_nums = set(nums)
        return len(unique_nums)==len(nums)
        