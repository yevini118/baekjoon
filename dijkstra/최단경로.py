import sys
from heapq import heappush, heappop

def dijkstra(start):

    Q = []
    heappush(Q, (0, start))
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


V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

INF = int(1e9)
distance = [INF] * (V + 1)

dijkstra(K)
for i in range(1, V+1):
    print(distance[i] if distance[i]<INF else 'INF')
