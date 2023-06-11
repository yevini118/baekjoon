X = int(input())

#bottom_up
count_bottom = [0] * (X+1)

for i in range(2, len(count_bottom)):
    minimum = count_bottom[i-1]

    if (i%2 == 0):
        minimum = min(minimum, count_bottom[i//2])
    if (i%3 == 0):
        minimum = min(minimum, count_bottom[i//3])

    count_bottom[i] = minimum + 1

print(count_bottom[X])

#top_down
count_top = {1:0}

def dp(num):
    if num in count_top:
        return count_top[num]
    
    if (num%2 == 0) and (num%3 == 0):
        count_top[num] =  min(dp(num//2), dp(num//3)) + 1
    elif (num%2 == 0):
        count_top[num] =  min(dp(num//2), dp(num-1)) + 1
    elif (num%3 == 0):
        count_top[num] =  min(dp(num//3), dp(num-1)) + 1
    else:
        count_top[num] =  dp(num-1) + 1
    return count_top[num]
    
print(dp(X))