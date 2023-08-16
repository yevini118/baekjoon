import sys
from collections import deque

N, M, V = map(int, input().split())
graph = {i:[] for i in range(1, N+1)}
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for n in graph:
    graph[n].sort()

visit_dfs = [False] * (N+1)
def dfs(node):
    
    visit_dfs[node] = True
    print(node, end=' ')
    for n in graph[node]:
        if visit_dfs[n] == False:
            dfs(n)


visit_bfs = [False] * (N+1)
visit_bfs[V] = True
def bfs(node):

    Q = deque([node])
    while(Q):
        node = Q.popleft()
        print(node, end=' ')

        for n in graph[node]:
            if visit_bfs[n] == False:
                visit_bfs[n] = True
                Q.append(n)

dfs(V)
print()
bfs(V)