import sys

T = int(input())

for t in range(T):
    
    N = int(input())
    
    parent = [0 for _ in range(N+1)]
    for _ in range(N-1):
        A, B = map(int, sys.stdin.readline().split())
        parent[B] = A

    N1, N2 = map(int, input().split())

    path = []
    while N1:
        path.append(N1)
        N1 = parent[N1]

    while N2:
        if N2 in path:
            print(N2)
            break
        N2 = parent[N2]