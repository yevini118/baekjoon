import sys
from heapq import heappop, heappush

direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]
num = 0
INF = int(1e9)

def dijkstra(x, y):

    Q = []
    heappush(Q, (jelda[y][x], x, y))

    while(Q):
        
        c, x, y = heappop(Q)

        if cost[y][x] < c:
            continue
        
        for a, b in direction:
            nx, ny = x + a, y + b
            if 0 <= nx < N and 0 <= ny < N:
                
                next_c = c + jelda[ny][nx]
                if next_c < cost[ny][nx]:
                    heappush(Q, (next_c, nx, ny))
                    cost[ny][nx] = next_c

while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break

    jelda = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    cost = [[INF] * N for _ in range(N)]
    dijkstra(0, 0)
    num += 1
    print("Problem {}: {}".format(num,cost[N-1][N-1]))