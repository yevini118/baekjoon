import sys
from collections import deque

N, M = map(int, input().split())
sea = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def bfs():

    Q = deque()

def next_year():

    new_sea = [[0] * M for _ in range(N)]
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for n in range(N):
        for m in range(M):
            count = 0
            if sea[n][m] != 0:
                for a, b in direction:
                    nn, nm = n+a, m+b
                    if 0<=nn<N and 0<=nm<M:
                        if sea[nn][nm] == 0:
                            count += 1
            if sea[n][m] - count > 0 :
                new_sea[n][m] = sea[n][m] - count
            else:
                new_sea[n][m] = 0

    return new_sea

year = 0
while(True):

    sea = next_year()
    year += 1

    for s in sea:
        print(s)

    if year == 2:
        break
