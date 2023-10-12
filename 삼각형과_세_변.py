def triangle(A, B, C):

    lines = sorted([A, B, C])
    if (lines[0] + lines[1] <= lines[-1]):
        return "Invalid"
    
    if A == B == C:
        return "Equilateral"
    
    if A != B and B != C and A != C:
        return "Scalene"
    
    return "Isosceles"

while(True):
    A, B, C = map(int, input().split())
    if A == B == C == 0:
        break

    print(triangle(A, B, C))


