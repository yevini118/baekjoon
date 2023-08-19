T = int(input())

def dp():

    #memory
    mem = [[0, sticker[i][0]] for i in range(2)]

    for y in range(1, n):

        #점화식 : 최대점수 = 자기점수 + max(한칸대각선 점수 , 두칸 대각선 점수)
        mem[0].append(sticker[0][y] + max(mem[1][-1], mem[1][-2]))  #윗줄
        mem[1].append(sticker[1][y] + max(mem[0][-2], mem[0][-3]))  #아래줄

    return max(mem[0][-1], mem[1][-1])
                
for i in range(T):

    #input
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]

    print(dp())