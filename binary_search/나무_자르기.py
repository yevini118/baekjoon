from collections import Counter

N, M = map(int, input().split())
trees = Counter(map(int, input().split()))

start = 0
end = max(trees)

while(start <= end):

    mid = (start + end) // 2
    total = sum((l-mid) * c for l, c in trees.items() if l>mid)

    if total < M:
        end = mid - 1
    else:
        start = mid + 1

print(start-1)