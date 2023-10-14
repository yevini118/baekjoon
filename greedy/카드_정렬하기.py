from heapq import heapify, heappush, heappop
import sys

N = int(input())
cards = [int(sys.stdin.readline()) for _ in range(N)]
heapify(cards)

total = 0
while(len(cards) > 1):
    
    c1 = heappop(cards)
    c2 = heappop(cards)
    heappush(cards, c1 + c2)
    total += c1 + c2
        
print(total)