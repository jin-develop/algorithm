N = int(input())
a, b = 0, 0
def fibo(n):
    a = 0
    b = 0
    if n == 0:
        a += 1
        return 0
    elif n== 1:
        b += 1
        
        return 1
    elif n == 2:
        return 1
    else:
        return fibo(n-2) + fibo(n-1)




fibo(N)
print(a,b)
