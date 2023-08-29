#input
N = int(input())
M = int(input())

# 아래 -> 오른쪽 -> 위 -> 왼쪽
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

board = [[0] * N for _ in range(N)]
index = 0
x, y = 0, 0

#큰수부터 채워나감
for i in range(N*N, 0, -1):

    board[y][x] = i

    #입력받은 자연수의 좌표
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

#output
for b in board:
    print(*b)
    
print(ay + 1, ax + 1)