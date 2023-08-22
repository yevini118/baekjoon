n = int(input())
nums = list(map(int, input().split()))

def dp():

    mem = [0] * n
    mem[0] = nums[0]

    for i in range(1, n):
        if mem[i-1] + nums[i] < nums[i]:
            mem[i] = nums[i]
        else:
            mem[i] = mem[i-1] + nums[i]

    return(max(mem))

print(dp())