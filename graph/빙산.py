import sys
from collections import deque

#input
N, M = map(int, input().split())
sea = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def bfs(n, m):

    Q = deque([(n,m)])
    visit[n][m] = True
    
    while(Q):

        n, m = Q.popleft()

        for a, b in direction:
            nn, nm = n+a, m+b

            if not visit[nn][nm]:
                if sea[nn][nm] == 0 and sea[n][m] > 0:
                    sea[n][m] -= 1

                if sea[nn][nm] != 0:
                    Q.append((nn, nm))
                    visit[nn][nm] = True

        #빙하가 다 녹으면
        if sea[n][m] == 0:
            ice.remove((n, m))


#상하좌우
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

#빙하 좌표 
ice = set()
for n in range(N):
    for m in range(M):
        if sea[n][m] > 0:
            ice.add((n, m))

year = 0
while(True):

    visit = [[False] * M for _ in range(N)]
    area = 0
    ice_copy = ice.copy()

    for n, m in ice_copy:
        if sea[n][m] != 0 and not visit[n][m]:
            bfs(n, m)
            area += 1

    if area >= 2:
        print(year)
        break
    if area == 0:
        print(0)
        break

    year += 1