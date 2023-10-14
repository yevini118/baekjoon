import sys

n = int(input())
k = int(input())
cards = [sys.stdin.readline().strip() for _ in range(n)]


def back(idx, depth, num):

    if depth == k:
        backs.add(num)
        return
    
    for i in range(n):

        if not visit[i]:
            visit[i] = True
            back(i, depth+1, num + cards[i])
            visit[i] = False

visit = [False] * n
backs = set()
back(0, 0, '')
print(len(backs))