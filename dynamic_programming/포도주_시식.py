import sys

n = int(input())

wine = [0]
for i in range(n):
    wine.append(int(sys.stdin.readline()))

score = [0] * (n+1)
score[1] = wine[1]

if n>1:
    score[2] = wine[1] + wine[2]
    for i in range(3, n+1):
        score[i] = max(score[i-2] + wine[i], score[i-3] + wine[i-1] + wine[i], score[i-1])

print(score[-1])
