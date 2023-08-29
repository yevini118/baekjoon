import sys

#input
board = [list(map(int, sys.stdin.readline().split())) for _ in range(19)]

def winner():

    for y in range(19):
        for x in range(19):
            if board[y][x] != 0:

                # ↓ 방향
                if y+4 < 19:
                    if not(y+5<19 and board[y+5][x] == board[y][x]) and not(y-1>=0 and board[y-1][x] == board[y][x]):
                        for i in range(1, 5):
                            if board[y+i][x] != board[y][x]:
                                break
                        else:
                            return(board[y][x], y, x)
                
                # → 방향
                if x+4 < 19:
                    if not(x+5<19 and board[y][x+5] == board[y][x]) and not(x-1>=0 and board[y][x-1] == board[y][x]):
                        for i in range(1, 5):
                            if board[y][x+i] != board[y][x]:
                                break
                        else:
                            return(board[y][x], y, x)

                # ↘ 방향
                if x+4<19 and y+4<19:
                    if not(x+5<19 and y+5<19 and board[y+5][x+5] == board[y][x]) and not(y-1>=0 and x-1>=0 and board[y-1][x-1] == board[y][x]):
                        for i in range(1, 5):
                            if board[y+i][x+i] != board[y][x]:
                                break
                        else:
                            return(board[y][x], y, x)

                # ↙ 방향
                if y+4<19 and x-4>=0:
                    if not(y+5<19 and x-5>=0 and board[y+5][x-5] == board[y][x]) and not(y-1>=0 and x+1<19 and board[y-1][x+1] == board[y][x]):
                        for i in range(1, 5):
                            if board[y+i][x-i] != board[y][x]:
                                break
                        else:
                            return(board[y][x], y+4, x-4) #가장왼쪽
    return (0, 0, 0)
                    
winner, x, y = winner()
print(winner)
if winner != 0:
    print(x+1, y+1)