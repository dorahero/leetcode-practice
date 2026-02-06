from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkValid(array):
            if len(set(array)) != len(array):
                return False
            for a in array:
                if int(a) < 1 or int(a) > 9:
                    return False
            return True
        for i in range(3):
            for j in range(3):
                sk = board[0 + 3 * i][j * 3: (j + 1) * 3] + board[1 + 3 * i][j * 3: (j + 1) * 3] + board[2 + 3 * i][j * 3: (j + 1) * 3]
                sk = [s for s in sk if s != '.']
                if not checkValid(sk):
                    return False
        for i in range(9):
            sk = [b for b in board[i] if b != '.']
            if not checkValid(sk):
                return False
            sk = [b[i] for b in board if b[i] != '.']
            if not checkValid(sk):
                return False
            
        return True

if __name__=="__main__":
    solution = Solution()
    test1 = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
    res = solution.isValidSudoku(test1)
    print(res)
    test2 = [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
    res = solution.isValidSudoku(test2)
    print(res)