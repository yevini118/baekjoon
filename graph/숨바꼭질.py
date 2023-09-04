from collections import deque

#input
N, K = map(int, input().split())

def bfs():
    
    if N >= K:
        return N-K
    
    limit = 100001
    visit = [0] * limit
    
    Q = deque([N])
    while(Q):
        
        X = Q.popleft()

        if X == K:
            return visit[K]
        
        for nx in ([X+1, X-1, 2*X]):
            if 0 <= nx < limit and visit[nx] == 0:
                visit[nx] = visit[X] + 1
                Q.append(nx)

print(bfs())