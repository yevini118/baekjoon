from collections import deque

#input
N, M = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(N)]

#방향설정
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

#BFS
def bfs():

    Q = deque([(0, 0)])
    while(Q):

        x, y = Q.popleft()

        #상하좌우
        for a, b in direction:
            nx, ny = x + a, y + b
            if 0 <= nx < N and 0 <= ny < M:
                if maze[nx][ny] == 1:
                    maze[nx][ny] = maze[x][y] + 1
                    Q.append((nx, ny))

        maze[0][0] = 0

bfs()
print(maze[N-1][M-1])   