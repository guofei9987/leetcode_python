# https://leetcode.com/problems/valid-sudoku
class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    board[i][j]=0
                else:
                    board[i][j]=int(board[i][j])
                    if board[i][j]>9 or board[i][j]<0:
                        return False
        # rule 1
        for i in range(9):
            if sum(set(board[i]))<sum(board[i]):
                return False
        # rule 2
        board_T=list(zip(*board))
        for i in range(9):
            if sum(set(board_T[i]))<sum(board_T[i]):
                return False
        # rule 3
        idxs=[[0,1,2],[3,4,5],[6,7,8]]
        for i in idxs:
            for j in idxs:
                tmp_list=[board[i1][j1] for i1 in i for j1 in j]
                if sum(set(tmp_list))<sum(tmp_list):
                    return False
        return True



board=[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]


Solution().isValidSudoku(board)

