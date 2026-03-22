import sys
input = sys.stdin.readline

n = int(input())

board = [[0]*n for _ in range(n)]
result = 0

def is_possible(row, col):
    for i in range(n):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i][j] == 1:
            return False
        
    return True
def n_queen(row):
    global result
    if row == n:
        result += 1
        return
    for col in range(n):
        if is_possible(row, col):
            board[row][col] = 1
            n_queen(row+1)
            board[row][col] = 0
n_queen(0)
print(result)



