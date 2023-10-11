import sys
from collections import deque

N, M = map(int, input().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
islands = [[0] * M for _ in range(N)]
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visit = [[False] * M for _ in range(N)]
bridge = []
unioned = set()

def bfs(node, area):

    Q  = deque([node])

    while(Q):

        x, y = Q.popleft()

        for a, b in direction:
            nx, ny = x + a, y + b
            if (0<= nx < M and 0<= ny < N):
                if maps[ny][nx] == 1 and not visit[ny][nx]:
                    visit[ny][nx] = True
                    Q.append((nx, ny))
                    islands[ny][nx] = area

def make_bridge(node):

    x, y = node
    for a, b in direction:
        step = 1
        while(True):
            nx, ny = x + a * step, y + b * step
            if (0<= nx < M and 0<= ny < N):
                if islands[ny][nx] == 0:
                    step += 1
                else:
                    step -= 1
                    if step > 1 and islands[y][x] != islands[ny][nx]:
                        bridge.append((islands[y][x], islands[ny][nx], step))
                    break
            else:
                break
                
def find(a):

    if a != parent[a]:
        parent[a] = find(parent[a])
    return a

def union(a, b):
    
    parent[find(b)] = find(a)

def isCycle(a, b):

    return find(a) == find(b)

area = 1
for x in range(M):
    for y in range(N):
        if maps[y][x] == 1 and not visit[y][x]:
            visit[y][x] = True
            islands[y][x] = area
            bfs((x,y), area)
            area += 1

parent = [p for p in range(0, area)]

for x in range(M):
    for y in range(N):
        if islands[y][x] != 0:
            make_bridge((x, y))

bridge.sort(key= lambda b : b[2])

total = 0
for a, b, length in bridge:

    if (not isCycle(a, b)):
        union(a, b)
        total += length

for i in range(1, area-1):
    if (not isCycle(i, i+1)):
        total = -1

print(total if total != 0 else -1)