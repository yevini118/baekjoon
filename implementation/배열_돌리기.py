import sys

T = int(input())

def rotate(num):

    mid = n//2
    left_diagonal, right_diagonal = [[i, i] for i in range(n)], [[i, n-i-1] for i in range(n)]  #주 대각선, 부 대각선
    col, row = [[i, mid] for i in range(n)], [[mid, i] for i in range(n)] #중간 열, 중간 행
    lines = [left_diagonal, col, right_diagonal, list(reversed(row)), list(reversed(left_diagonal)), list(reversed(col)), list(reversed(right_diagonal)), row]
    
    new_board = [[0] * n for _ in range(n)]

    #rotate
    for i in range(len(lines)):

        target = lines[i]
        to = lines[(i + num) % len(lines)]

        for j in range(n):
            new_board[to[j][0]][to[j][1]] = board[target[j][0]][target[j][1]]
    
    #제자리인 애들을 채워줌
    for x in range(n):
        for y in range(n):
            if new_board[y][x] == 0:
                new_board[y][x] = board[y][x]

    return new_board
       

for t in range(T):
    n, d = map(int,input().split())
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    if d%360 == 0:
        new_board = board
    else:
        new_board = rotate(d//45)
        
    for l in new_board:
        print(*l)