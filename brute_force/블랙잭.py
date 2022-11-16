from itertools import combinations

n, m = map(int, input().split())
card = list(map(int, input().split()))

card_sum = [sum(c) for c in combinations(card, 3) if sum(c)<=m]

print(max(card_sum))