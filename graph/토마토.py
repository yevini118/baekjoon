import sys
from collections import deque

M, N = map(int, input().split())
store = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]

Q = deque([])
for i in range(N):
    for j in range(M):
        if store[i][j] == 1:
            Q.append((i, j))

while(Q):

    x, y = Q.popleft()

    for a, b in direction:
        nx, ny = x+a, y+b
        if 0 <= nx < N and 0 <= ny < M:
            if store[nx][ny] == 0:
                store[nx][ny] = store[x][y]+1
                Q.append((nx, ny))

answer = 0
for s in store:
    if 0 in s:
        answer = 0
        break

    if max(s) > answer:
        answer = max(s)

print(answer-1)