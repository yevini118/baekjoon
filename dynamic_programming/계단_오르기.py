#input
N = int(input())
stair = [0, 0] + [int(input()) for _ in range(N)]

#최고점수 memory
score = stair[:3]

def dp():

    #점화식 : i의 최고점수 = i점수 + max(i-2의 최고점수 , i-3의 최고점수 + i-2점수) 
    for i in range(3, N+2):
        score.append(stair[i] + max(score[i-2], score[i-3] + stair[i-1]))

dp()
print(score[-1])