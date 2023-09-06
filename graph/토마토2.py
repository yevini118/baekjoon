import sys
from collections import deque

M, N, H = map(int, input().split())
tomatos = [[list(map(int, sys.stdin.readline().split())) for n in range(N)] for h in range(H)]

#6방
direction = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

def bfs(nodes):

    day = 0
    Q = deque(nodes)

    while(Q):
        length = len(Q)
        for i in range(length):
            h, y, x = Q.popleft()

            for c, b, a in direction:

                nh, ny, nx = h+c, y+b, x+a
                if 0<= nh < H and 0<= ny < N and 0<= nx < M:
                    if tomatos[nh][ny][nx] == 0:
                        tomatos[nh][ny][nx] = tomatos[h][y][x] + 1
                        Q.append((nh, ny, nx))
        day += 1

    # 안 익은 토마토가 있으면 return -1
    for h in range(H):
        for y in range(N):
            if 0 in tomatos[h][y]:
                return -1
    
    return day


#익은 토마토 좌표를 bfs 큐로 넣어줌
nodes = []
for h in range(H):
    for y in range(N):
        for x in range(M):
            if tomatos[h][y][x] == 1:
                nodes.append((h, y, x))
                
print(bfs(nodes))