n = int(input())

mem = [0, 1, 2]

for i in range(3, n+1):
    mem.append(mem[i-1] + mem[i-2])

print(mem[n] % 10007)