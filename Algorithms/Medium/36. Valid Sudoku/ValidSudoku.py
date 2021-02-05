class Solution(object):
    def isValidSudoku(self, board):
        def checksquare(sudoku):
            for i in range(3):
                for j in range(3):
                    res = []
                    for k in range(3):
                        res += sudoku[k+j*3][i*3:(i+1)*3]
                    counter = 0
                    _ = set()
                    for r in res:
                        if r != ".":
                            counter += 1
                            _.add(r)
                    if counter != len(_):
                        return False
            return True

        ans = True
        if not checksquare(board):
            ans = False
            return ans
        for b in board:
            _ = set()
            counter = 0
            for i in b:
                if i != ".":
                    counter += 1
                    _.add(i)
            if counter != len(_):
                ans = False
                return ans
        for x in range(9):
            _ = set()
            counter = 0
            for y in range(9):
                if board[y][x] != ".":
                    counter += 1
                    _.add(board[y][x])
                if counter != len(_):
                    ans = False
                    return ans
        return ans
if __name__ == "__main__":
    board = [[".",".","4",".",".",".","6","3","."]
            ,[".",".",".",".",".",".",".",".","."]
            ,["5",".",".",".",".",".",".","9","."]
            ,[".",".",".","5","6",".",".",".","."]
            ,["4",".","3",".",".",".",".",".","1"]
            ,[".",".",".","7",".",".",".",".","."]
            ,[".",".",".","5",".",".",".",".","."]
            ,[".",".",".",".",".",".",".",".","."]
            ,[".",".",".",".",".",".",".",".","."]]
    res = Solution().isValidSudoku(board)
    print(res)