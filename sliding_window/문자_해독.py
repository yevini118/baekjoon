g, s = map(int, input().split())
W = input()
S = input()

W_count = [0] * 58
S_count = [0] * 58

for i in W:
    W_count[ord(i) - 65] += 1

left, right = 0, g-1
for i in range(left, right):
    S_count[ord(S[i]) - 65] += 1

count = 0
while right < s:

    S_count[ord(S[right]) - 65] += 1

    if W_count == S_count:
        count += 1

    S_count[ord(S[left]) - 65] -= 1

    left += 1
    right += 1
    
print(count)