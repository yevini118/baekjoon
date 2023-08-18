T = int(input())
N = [int(input()) for _ in range(T)]

#memory
P = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

def dp(N):
    
    #점화식 : P[i] = P[i-1] + P[i-5]
    for i in range(len(P), N):
        P.append(P[i-1] + P[i-5])
    
    return P[N-1]

for n in N:
    print(dp(n))