from collections import deque

n = int(input())
m = int(input())
pairs = {i:[] for i in range(1, n+1)}

for i in range(m):
    a,b = map(int, input().split())
    pairs[a].append(b)
    pairs[b].append(a)

#dfs
visit_dfs = [0] * (n+1)
def dfs(node):
    visit_dfs[node] = 1
    for p in pairs[node]:
        if visit_dfs[p] == 0:
            dfs(p)

dfs(1)
print(sum(visit_dfs) - 1)

#bfs
visit_bfs = [0] * (n+1)
visit_bfs[1] = 1
def bfs():
    queue = deque([1])
    while queue:
        c = queue.popleft()
        for p in pairs[c]:
            if visit_bfs[p] == 0:
                queue.append(p)
                visit_bfs[p] = 1

bfs()
print(sum(visit_bfs) - 1)