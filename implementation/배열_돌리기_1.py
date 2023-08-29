import sys

#input
N, M, R = map(int, input().split())
array = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def rotate(R):

    lines = []

    #rotate될 line의 수
    depth = min(N, M)//2
    for i in range(depth):
        line = []
        # ↓ 방향
        for j in range(i, N-i-1): 
            line.append(array[j][i])
        # → 방향
        for j in range(i, M-i-1):
            line.append(array[N-1-i][j])
        # ↑ 방향
        for j in range(N-1-i, i, -1):
            line.append(array[j][M-1-i])
        # ← 방향
        for j in range(M-1-i, i, -1):
            line.append(array[i][j])
        lines.append(line)


    for i in range(depth):

        #line배열을 -R부터 순회
        length = len(lines[i])
        index = -R
        for j in range(i, N-i-1): 
            array[j][i] = lines[i][index%length]
            index += 1

        for j in range(i, M-i-1):
            array[N-1-i][j] = lines[i][index%length]
            index += 1

        for j in range(N-1-i, i, -1):
            array[j][M-1-i] = lines[i][index%length]
            index += 1

        for j in range(M-1-i, i, -1):
            array[i][j] = lines[i][index%length]
            index += 1

rotate(R)
for a in array:
    print(*a)