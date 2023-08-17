import sys
from collections import deque

N = int(input())
apart = [list(sys.stdin.readline().strip()) for _ in range(N)]

#방향설정
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

#DFS
def dfs(x, y):

    global count
    count += 1

    apart[y][x] = '0'

    for a, b in direction:
        nx, ny = x + a, y + b
        if 0 <= nx < N and 0 <= ny < N:
            if apart[ny][nx] == '1':
                dfs(nx, ny) 

#BFS
def bfs(x, y):

    Q = deque([(x, y)])
    apart[y][x] = '0'
    count = 1

    while(Q):
        x, y = Q.popleft()

        for a, b in direction:
            nx, ny = x + a, y + b
            if 0 <= nx < N and 0 <= ny < N:
                if apart[ny][nx] == '1':
                    apart[ny][nx] = '0'
                    Q.append((nx, ny))
                    count += 1

    return count
        

#방문안한 단지확인
global count
answer = []
for x in range(N):
    for y in range(N):
        count = 0
        if apart[y][x] == '1':
                dfs(x, y)
                answer.append(count)
                # answer.append(bfs(x, y))
answer.sort()

print(len(answer))
for a in answer:
    print(a)