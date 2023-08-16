import sys
from collections import deque

read = sys.stdin.readline

M, N, H = map(int, input().split())
store = [[list(map(int, read().split())) for i in range(N)] for h in range(H)]

Q = deque([])
for h in range(H):
    for n in range(N):
        for m in range(M):
            if store[h][n][m] == 1:
                Q.append((n, m, h))

day = -1

while(Q):
    lenQ = len(Q)
    for i in range(lenQ):
        n, m, h = Q.popleft()

        if n+1 < N and store[h][n+1][m] == 0:
            store[h][n+1][m] = 1
            Q.append((n+1, m, h))
        if n-1 >= 0 and store[h][n-1][m] == 0:
            store[h][n-1][m] = 1
            Q.append((n-1, m, h))
        if m+1 < M and store[h][n][m+1] == 0:
            store[h][n][m+1] = 1
            Q.append((n, m+1, h))
        if m-1 >= 0 and store[h][n][m-1] == 0:
            store[h][n][m-1] = 1
            Q.append((n, m-1, h))
        if h+1 < H and store[h+1][n][m] == 0:
            store[h+1][n][m] = 1
            Q.append((n, m, h+1))
        if h-1 >= 0 and store[h-1][n][m] == 0:
            store[h-1][n][m] = 1
            Q.append((n, m, h-1))
        
    day += 1


for s in store:
    for n in range(N):
        if 0 in s[n]:
            day = -1
            break

print(day)