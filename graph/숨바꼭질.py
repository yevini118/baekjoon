from collections import deque

N, K = map(int, input().split())

if N >= K :
    print(N-K)

else:

    limit = 100001
    visit = [0] * limit
    Q = deque([N])

    while(Q):
        X = Q.popleft()
        if X==K:
            break
            
        for nx in [X-1, X+1, 2*X]:
            if 0 <= nx < limit:
                if visit[nx] == 0:
                    Q.append(nx)
                    visit[nx] = visit[X] + 1
                    
    print(visit[K])      
