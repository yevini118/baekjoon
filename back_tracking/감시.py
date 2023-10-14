import sys
import copy

N, M = map(int, input().split())
room = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

left, right, up, down = (1, 0) , (-1, 0), (0, 1), (0, -1)
cctv = {1: [[left], [right], [up], [down]], 
        2: [[left, right],[up, down]], 
        3 : [[up, right], [right, down], [down, left], [left, up]], 
        4: [[left, up, right], [up, right, down], [left, down, right], [up, left, down]],
        5:[[left, right, up, down]]}


def back(depth, room):

    global answer
    
    if depth == len(cctvs):
        answer = min(answer, nosight(room))
        return
    
    room_copy = copy.deepcopy(room)
    n, x, y = cctvs[depth]
    for direction in cctv[n]:
        sight((x, y), direction, room_copy)
        back(depth + 1, room_copy)
        room_copy = copy.deepcopy(room)

def sight(now, direction, room):

    for d in direction:

        nx, ny = now
        a, b = d

        while(True):

            nx += a 
            ny += b
            if 0 <= nx < M and 0 <= ny < N:
                if room[ny][nx] == 6:
                    break
                if room[ny][nx] == 0:
                    room[ny][nx] = -1
            else:
                break

def nosight(room):

    count = 0
    for y in range(N):
        for x in range(M):
            if room[y][x] == 0:
                count += 1

    return count

answer = int(1e9)
cctvs = []
for y in range(N):
    for x in range(M):
        if 0 < room[y][x] < 6:
            cctvs.append((room[y][x], x, y))

back(0, room)
print(answer)