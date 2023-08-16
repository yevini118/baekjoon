n = int(input())

stairs = [0]
for i in range(n):
    stairs.append(int(input()))

score = [0] * (n+1)
score[1] = stairs[1]

if n>1:
    score[2] = stairs[1] + stairs[2]
    for i in range(3, n+1):
        score[i] = max(score[i-2], stairs[i-1] + score[i-3]) + stairs[i]

print(score[-1])