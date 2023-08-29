import sys

#input
N = int(input())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(N*N)]

scores = [0, 1, 10, 100, 1000]
side = [(0, 1), (0, -1), (1, 0), (-1, 0)]
seat = [[0]*N for _ in range(N)]

#자리배치
def arrangement():

    for t in table:
        student = t[0]
        likes = t[1:]

        comp = []
        for x in range(N):
            for y in range(N):
                if seat[y][x] == 0:
                    empty = 0
                    like = 0

                    for a, b in side:
                        nx, ny = x + a, y + b
                        if 0<=nx<N and 0<= ny<N:
                            if seat[ny][nx] in likes:
                                like += 1
                            if seat[ny][nx] == 0:
                                empty += 1
                    comp.append([x, y, like, empty])
        
        #인접한 좋아하는 친구수 내림차순-> 빈칸수 내림차순-> 행 오름차순-> 열 오름차순 으로 정렬
        comp.sort(key= lambda c: (-c[2], -c[3], c[1], c[0]))
        x, y = comp[0][0], comp[0][1]

        seat[y][x] = student
    
#점수계산
def calculate():

    score = 0
    for t in table:
        student = t[0]
        likes = t[1:]

        for x in range(N):
            for y in range(N):
                if seat[y][x] == student:
                    like = 0

                    for a, b in side:
                        nx, ny = x + a, y + b
                        if 0<=nx<N and 0<= ny<N:
                            if seat[ny][nx] in likes:
                                like += 1

        score += scores[like]
    
    return score

arrangement()
print(calculate())