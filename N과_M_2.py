from itertools import combinations

N, M = map(int, input().split())

nums = [str(i) for i in range(1, N+1)]
answer = combinations(nums, M)

for a in answer:
    print(*a)