import math

M, N = map(int, input().split())

#Eratos
def is_prime_number(num) :
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if (num % i == 0):
            return False
    return True

for i in range(M, N+1):
    if is_prime_number(i):
        print(i)

#Eratos_optimization
is_prime = [True] * (N+1)
is_prime[0] = False
is_prime[1] = False

def set_prime_number(num):
    for i in range(2, int(num ** 0.5)+1):
        if is_prime[i]:
            for j in range(2, num//i+1):
                is_prime[i*j] = False

set_prime_number(N)
for i in range(M, N+1):
    if is_prime[i]:
        print(i)




