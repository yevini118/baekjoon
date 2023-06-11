n = int(input())

title = "666"
num = 666
count = 1
while(count<n):
    num += 1
    if title in str(num):
        count += 1

print(num)
