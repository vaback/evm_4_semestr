class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        def find(i, j, k):
            if (i < 0 or i >= m) or (j < 0 or j >= n): return False
            if board[i][j] != word[k]: return False
            if k == (len(word)-1): return True
            
            temp = board[i][j]
            board[i][j] = '#'

            res = (find(i +1, j, k + 1) or
                    find(i -1, j, k + 1) or
                    find(i, j + 1, k + 1) or
                    find(i, j - 1, k + 1))

            board[i][j] = temp
            return res

        for i in range(m):
            for j in range(n):
                if(word[0] == board[i][j]):
                    if find(i, j, 0):
                        return True


        return False