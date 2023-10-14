N = int(input())
s, grage, p, d = map(int, input().split())
MVP = input()

moneys = {'B':s-1, 'S':grage-1, 'G':p-1, 'P':d-1, 'D':d}

total = 0
last = 0
for grage in MVP:
    if grage == 'D':
        last = moneys[grage]
    else:
        last = moneys[grage] - last
    total += last

print(total)