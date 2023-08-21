#input
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

def dp():

    #memory
    mem = [0] * (k+1)
    mem[0] = 1

    for c in coins:
        for i in range(k+1):
            if i-c >= 0:
                #점화식 : mem[i] = mem[i] + mem[i-c]
                mem[i] += mem[i-c]

    return mem[k]

print(dp())
