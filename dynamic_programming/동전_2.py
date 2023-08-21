#input
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

def dp():

    mem = [99999] * (k+1)
    mem[0] = 0
    
    for c in coins: 
        for i in range(k+1):
            if i-c >=0:
                #점화식
                mem[i] = min(mem[i], mem[i-c] + 1)
    
    return -1 if mem[k] == 99999 else mem[k]

print(dp())