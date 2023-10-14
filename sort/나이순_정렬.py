import sys

N = int(input())
peoples = [list(sys.stdin.readline().split()) for _ in range(N)]

peoples.sort(key = lambda x: int(x[0]))
for p in peoples:
    print(*p)