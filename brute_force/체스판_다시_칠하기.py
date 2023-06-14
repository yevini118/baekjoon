n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(input())

color = {'W':'B', 'B':'W'}

cost = 0
for i in range(m-1):
    if board[0][i] == board[0][i+1]:
        cost += 1
        board[0][i+1] = color[board[0][i+1]]



        

    


