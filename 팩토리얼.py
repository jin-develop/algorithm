# n = 10
n = int(input())

def fac(n):
    if n==0:
        return 0
    elif n == 1:
        return 1
    return n * fac(n-1)

print(fac(n))

N = int(input())
 
def factorial(N):
    if N == 0:
        return 1
    elif N == 1:
        return 1
    return N * factorial(N-1)
 
print(factorial(N))