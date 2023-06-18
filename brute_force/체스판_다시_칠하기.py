N, M = map(int, input().split())

board = []
for i in range(N):
    board.append(input())

W = [[0] * M for i in range(N)]
B = [[0] * M for i in range(N)]
count = []

def set_change_board():
    for x in range(N):
        for y in range(M):
            if (x%2==0 and y%2==0) or (x%2!=0 and y%2!=0):
                if board[x][y] != 'W':
                    W[x][y] = 1
                else:
                    B[x][y] = 1

            else:
                if board[x][y] != 'B':
                    W[x][y] = 1
                else:
                    B[x][y] = 1

def count_change():
    for x in range(N-7):
        for y in range(M-7):
            c_w = 0
            c_b = 0
            for i in range(8):
                c_w += sum(W[x+i][y:y+8])
                c_b += sum(B[x+i][y:y+8])
            count.append(c_w)
            count.append(c_b)

set_change_board()
count_change()
print(min(count))