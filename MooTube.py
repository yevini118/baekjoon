import sys
from collections import deque

N, Q = map(int, input().split())
USADO = {i:[] for i in range(1, N+1)}
for _ in range(N-1):
    p, q, r = map(int, sys.stdin.readline().split())
    USADO[p].append((q, r))
    USADO[q].append((p, r))
    
def bfs(k, v):

    visit = [False] * (N+1)
    Q = deque([v])
    visit[v] = True
    answer = 0

    while(Q):

        v = Q.popleft()
        for node, usado in USADO[v]:
            if usado >= k and not visit[node]:
                answer += 1
                Q.append(node)
                visit[node] = True

    return answer

for _ in range(Q):
    k, v = map(int, sys.stdin.readline().split())
    print(USADO)
    print(bfs(k, v))