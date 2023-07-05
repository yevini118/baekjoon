from collections import deque
import sys

def bfs(X, Y):

    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    Q = deque([(X, Y)])

    while(Q):
        X, Y = Q.popleft()

        if ground[Y][X] == 1:
            ground[Y][X] = 0

        for a, b in direction:
            nx, ny = X+a, Y+b
            if 0 <= nx < M and 0 <= ny < N:
                if ground[ny][nx] == 1:
                    ground[ny][nx] = 0
                    Q.append((nx, ny))

T = int(input())

for i in range(T):
    M, N, K = map(int, input().split())
    ground = [[0] * M for _ in range(N)]

    for k in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        ground[Y][X] = 1

    area = 0
    for n in range(N):
        for m in range(M):
            if ground[n][m] == 1:
                area += 1
                bfs(m, n)

    print(area)