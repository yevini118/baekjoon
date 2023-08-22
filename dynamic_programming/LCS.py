A = input()
B = input()

A = '0' + A
B = '0' + B

def dp():
    mem = [[0] * len(A) for _ in range(len(B))]

    for b in range(1, len(B)):
        for a in range(1, len(A)):
            if B[b] == A[a]:
                mem[b][a] = mem[b-1][a-1] + 1
            else:
                mem[b][a] = max(mem[b-1][a] , mem[b][a-1])

    return mem[-1][-1]

print(dp())