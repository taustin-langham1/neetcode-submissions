class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows, cols = len(board), len(board[0])
        visited = set()

        # column check
        c = 0
        while c < cols:
            for r in range(rows):
                    val = board[r][c]
                    if val == ".":
                        continue
                    elif val not in visited:
                        visited.add(val)
                    else:
                        return False
                    
            visited.clear()
            c+=1

        # row check
        r = 0
        while r < rows:
            for c in range(cols):
                    val = board[r][c]
                    if val == ".":
                        continue
                    elif val not in visited:
                        visited.add(val)
                    else:
                        return False
                    
            visited.clear()
            r+=1

        # 3x3 check

        row_start, col_start = 0, 0
        
        for row_start in range(0, 9, 3):
            for col_start in range(0, 9, 3):
                visited.clear()
                for i in range(3):
                    for j in range(3):
                        val = board[row_start + i][col_start + j]
                        if val == ".":
                            continue
                        elif val not in visited:
                            visited.add(val)
                        else: 
                            return False

        return True