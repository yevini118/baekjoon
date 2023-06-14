from collections import deque

N , M= map(int, input().split())

maze = []
for i in range(N):
    maze.append(input())

direction = [[0, -1],[0, 1], [-1, 0],[1, 0]]

#bfs
Q = deque([(0,0)])
visit = [[0]*M for i in range(N)]
visit[0][0] = 1

while(Q):
    x, y = Q.popleft()

    for d in direction:
        nx, ny = x + d[0], y + d[1]
        if nx < 0 or nx >= N or ny < 0 or ny >= M :
            continue
        
        if maze[nx][ny] == '1' and visit[nx][ny] == 0:
                visit[nx][ny] = visit[x][y] + 1
                Q.append((nx, ny))

print(visit[N-1][M-1])
        

