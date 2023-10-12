import sys
from heapq import heappush, heappop

def dijkstra(start):

    distance = [INF] * (N+1)

    Q = []
    heappush(Q, (0 ,start))
    distance[start] = 0

    while(Q):

        dist, node = heappop(Q)

        if distance[node] < dist:
            continue

        for n, d in graph[node]:
            cost = dist + d
            if cost < distance[n]:
                distance[n] = cost
                heappush(Q, (cost, n))
    
    return distance


N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]

for i in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())

INF = int(1e9)

dijk_1 = dijkstra(1)
dijk_v1 = dijkstra(v1)
dijk_v2 = dijkstra(v2)

path1 = dijk_1[v1] + dijk_v1[v2] + dijk_v2[N]
path2 = dijk_1[v2] + dijk_v2[v1] + dijk_v1[N]

answer = min(path1, path2)
print(answer if answer < INF else -1)