import sys
from collections import deque

N = int(input())
area = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

#상하좌우
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(node):

    Q = deque([node])
    while(Q):

        x, y = Q.popleft()

        for a, b in direction:
            nx, ny = x+a, y+b
            if 0 <= nx < N and 0 <= ny < N:
                if not visit[ny][nx]:
                    visit[ny][nx] = True
                    Q.append((nx, ny))

for 

visit = [[False] * N for _ in range(N)]

for y in range(N):
    for x in range(N):
        if visit[y][x] <= rain:
            visit[y][x] = False
        
