from collections import deque
import sys

#input
F, S, G, U, D = map(int, sys.stdin.readline().split())

direction = []
if U != 0:
    direction.append(U)
if D != 0:
    direction.append(-D)

def bfs():
    
    visit = [False] * (F+1)
    visit[S] = True
    step = [0] * (F+1)
    
    Q = deque([S])
    while(Q):

        x = Q.popleft()

        if x == G:
            return step[G]
        
        for a in direction:
            nx = x + a
            if 1 <= nx <= F and not visit[nx]:
                step[nx] = step[x] + 1
                visit[nx] = True
                Q.append(nx)
    
    return 'use the stairs'

print(bfs())