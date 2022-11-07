n, k = map(int, input().split())
coins = []

for i in range(n):
    coins.append(int(input()))

answer = 0

for i in range(n-1,-1, -1):
    answer += k // coins[i]
    k %= coins[i]

print(answer)

