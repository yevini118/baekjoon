n = int(input())
length = list(map(int, input().split()))
price = list(map(int, input().split()))

cost = 0
oiling = 0

while(oiling < n-1):

    for i in range(oiling+1, n):
        if price[oiling] > price[i]:
            break
    cost += sum(length[oiling:i]) * price[oiling]
    oiling = i
    
print(cost)

