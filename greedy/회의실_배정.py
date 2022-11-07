n = int(input())
meetings = []

for i in range(n):
    meeting = list(map(int, input().split()))
    meetings.append(meeting)

meetings.sort(key= lambda x: (x[1], x[0]))

answer = 0
before = [0,0]
for m in meetings:
    if m[0] >= before[1]:
        before = m
        answer += 1

print(answer)
