import sys
from collections import deque

#input
n = int(input())
m = int(input())
computer = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

#방문확인
visit = [0] * (n+1)
visit[1] = 1

#양방향 그래프 생성
graph = {i : [] for i in range(1, n+1)}
for a, b in computer:
    graph[a].append(b)
    graph[b].append(a)

#BFS
def bfs():
    Q = deque([1])

    while(Q):
        node = Q.popleft()
        for n in graph[node]:
            if visit[n] == 0:
                visit[n] = 1
                Q.append(n)

#DFS
def dfs(node):
    
    visit[node] = 1
    for n in graph[node]:
        if visit[n] == 0:
            dfs(n)

bfs()
# dfs(1)
print(sum(visit)-1)
                