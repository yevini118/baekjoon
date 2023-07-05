from collections import deque
from collections import Counter

T = int(input())

def solution(arr):

    if Counter(P)['D'] > n:
        return 'error'
    
    count = 0
    for p in P:
        if p == 'R':
            count += 1
        elif p == 'D':
            if count % 2 == 0:
                arr.popleft()
            else:
                arr.pop()

    if count % 2 == 1:
        arr.reverse()
        
    return '['+ ','.join(arr) +']'

for t in range(T):
    P = input().replace('RR','')
    n = int(input())
    arr = input()
    if 0 < n:
        arr = deque(list(arr.strip("[]").split(',')))
    else:
        arr = []
    
    print(solution(arr))