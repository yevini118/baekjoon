import sys

N = int(input())
words = [sys.stdin.readline().strip() for i in range(N)]

words = list(set(words))
words.sort(key= lambda w : (len(w), w))

print('\n'.join(words))