from collections import deque
import sys

N, M = map(int, input().split())
graph = {i:[] for i in range(1, N+1)}

for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visit = [False] * (N+1)
def bfs(node):

    visit[node] = True

    Q = deque([node])
    while(Q):
        node = Q.popleft()

        for n in graph[node]:
            if not visit[n]:
                visit[n] = True
                Q.append(n)        

component = 0
for n in range(1, N+1):
    if not visit[n]:
        component += 1
        bfs(n)

print(component)