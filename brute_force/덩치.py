n = int(input())
people = []
for i in range(n):
    people.append(list(map(int, input().split())))

for p1 in people:
    score = 1
    for p2 in people:
        if p1[0] < p2[0] and p1[1] < p2[1]:
            score +=1

    print(score, end=" ")
