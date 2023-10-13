import sys

def find(a):

    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):

    parent[find(b)] = find(a)
    print(parent)

def is_union(a, b):

    if find(a) == find(b):
        print('YES')
    else:
        print('NO')


n, m = map(int, input().split())
parent = [i for i in range(n+1)]
for _ in range(m):
    f, a, b = map(int, sys.stdin.readline().split())

    if f == 0:
        union(a, b)
    else:
        is_union(a, b)