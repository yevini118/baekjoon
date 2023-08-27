N = int(input())
M = int(input())

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

board = [[0] * N for _ in range(N)]
index = 0
x, y = 0, 0

for i in range(N*N, 0, -1):

    board[y][x] = i

    if i == M:
        ax, ay = x, y

    a, b = direction[index]
    nx, ny = x + a, y + b

    if nx < 0 or nx >= N or ny < 0 or ny >= N or board[ny][nx] != 0:
        
        index += 1
        if index == len(direction):
            index = 0
        
    a, b = direction[index]
    x, y = x + a, y + b

for b in board:
    print(*b)
    
print(ay + 1, ax + 1)