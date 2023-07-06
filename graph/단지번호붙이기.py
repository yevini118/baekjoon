from collections import deque

N = int(input())

map = []
for i in range(N):
    map.append(list(input()))

direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def bfs(x, y):

    count = 1
    Q = deque([(x, y)])
    map[x][y] = '0'

    while(Q):
        x, y = Q.popleft()

        for dx, dy in direction:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N:
                if map[nx][ny] == '1':
                    map[nx][ny] = '0'
                    count += 1
                    Q.append((nx, ny))
    return count

answer = []
for x in range(N):
    for y in range(N):
        if map[x][y] == '1':
            answer.append(bfs(x, y))

print(len(answer))
answer.sort()
for a in answer:
    print(a)