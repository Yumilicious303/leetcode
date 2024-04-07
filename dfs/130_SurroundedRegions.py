#Surrounded Regions
from _130_testCases import *

def solve(board):
    def dfs(r, c, direction):
        if (r, c) in notSurrounded:
            return True
        if (r >= rows or 
            c >= cols or
            c < 0 or
            r < 0):
                return True
        if board[r][c] == 'X':
            return False
        
        if direction == 'rightdown':
            if dfs(r + 1, c, 'rightdown') or dfs(r, c + 1, 'rightdown'): 
                notSurrounded.add((r, c))
                return True
            else: return False

        if direction == 'leftup':
            if dfs(r - 1, c, 'leftup') or dfs(r, c - 1, 'leftup'):
                notSurrounded.add((r, c))
                return True
            else: return False

        if direction == 'leftdown':
            if dfs(r - 1, c, 'leftdown') or dfs(r, c + 1, 'leftdown'):
                notSurrounded.add((r, c))
                return True
            else: return False

        if direction == 'rightup':
            if dfs(r + 1, c, 'rightup') or dfs(r, c - 1, 'rightup'):
                notSurrounded.add((r, c))
                return True
            else: return False

    
    notSurrounded = set()
    rows, cols = len(board), len(board[0])
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O':
                if not dfs(r, c, 'rightdown') and not dfs(r, c, 'leftup') and not dfs(r, c, 'leftdown') and not dfs(r, c, 'rightup'):
                    board[r][c] = 'X'


def solveNeet(board):
    def dfs(r, c):
        if (r >= rows or 
            c >= cols or
            c < 0 or
            r < 0 or 
            board[r][c] != 'O'):
            return
        board[r][c] = 'A'
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    rows, cols = len(board), len(board[0])
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O' and (r in [0, rows - 1] or c in [0, cols - 1]):
                dfs(r,c)

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O':
                board[r][c] = 'X'

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'A':
                board[r][c] = 'O'
    
                                               
        

solveNeet(board4)

if board4 == expected_board4:
    print('Passed')
else:
    print('Failed')