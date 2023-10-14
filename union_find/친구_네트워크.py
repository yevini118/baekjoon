import sys

def find(a):

    if parent[a] != a:
        parent[a] = find(parent[a])

    return parent[a]

def union(a, b):

    x = find(a)
    y = find(b)

    if x != y:
        parent[y] = x
        count[x] += count[y]

    print(count[x])

T = int(input())
for t in range(T):

    F = int(input())

    parent, count = {}, {}

    for _ in range(F):

        A, B = sys.stdin.readline().strip().split()
        
        if A not in parent:
            parent[A] = A
            count[A] = 1
        if B not in parent:
            parent[B] = B
            count[B] = 1

        union(A, B)
