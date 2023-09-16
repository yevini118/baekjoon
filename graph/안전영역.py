import sys
from collections import deque

N = int(input())
region = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def bfs(node, rain):

    #상하좌우
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    Q = deque([node])
    while(Q):

        x, y = Q.popleft()

        for a, b in direction:
            nx, ny = x+a, y+b
            if 0 <= nx < N and 0 <= ny < N:
                if not visit[ny][nx] and region[ny][nx] > rain:
                    visit[ny][nx] = True
                    Q.append((nx, ny))

import time

areas = [0]
for rain in range(0, 101):

    visit = [[False] * N for _ in range(N)]
    area = 0
    for y in range(N):
        for x in range(N):
            if not visit[y][x] and region[y][x] > rain:
                area += 1
                bfs((x, y), rain)

    areas.append(area)
end = time.time()

print(max(areas))