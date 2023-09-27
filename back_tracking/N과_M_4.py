from itertools import combinations

N, M = map(int, input().split())
nums = [0] * M

def back(start, depth):

    if depth == M:
        print(" ".join(nums))
        return

    for i in range(start, N+1):
        nums[depth] = str(i)
        back(i, depth+1)

back(1, 0)