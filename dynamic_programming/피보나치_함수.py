T = int(input())

mem = []
mem.append([1, 0])
mem.append([0, 1])

for i in range(2, 41):
    mem.append([mem[i-1][0] + mem[i-2][0], mem[i-1][1] + mem[i-2][1]]) 

for t in range(T):

    N = int(input())
    print(mem[N][0], mem[N][1])