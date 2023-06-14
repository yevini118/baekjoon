n = int(input())

for constructor in range(1, n):
    if n == constructor + sum(map(int, str(constructor))):
        print(constructor)
        break

else:
    print("0")

