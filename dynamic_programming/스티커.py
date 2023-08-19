T = int(input())

def dp():

    for y in range(2, n):
        for x in range(2):
            mem[x].append(sticker[x][y] + max(max(mem[x][:y-1]), max(mem[x-1][:y])))
                
for i in range(T):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    mem = [[sticker[0][0], sticker[0][1] + sticker[1][0]], [sticker[1][0], sticker[1][1] + sticker[0][0]]]

    dp()
    print(max(mem[0][n-1], mem[1][n-1]))
