N, S = map(int, input().split())
nums = list(map(int, input().split()))

def back(index, sum):

    global count
    if index == N:
        if sum == S:
            count += 1
        return

    back(index + 1, sum)
    back(index + 1, sum + nums[index])

count = 0
back(0, 0)
if S == 0:
    count -= 1
print(count)