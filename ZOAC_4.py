import math

H, W, N, M = map(int, input().split())

people = 0

h = math.ceil(H / (N + 1))
w = math.ceil(W / (M + 1))

print(h*w)