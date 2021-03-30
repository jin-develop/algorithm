'''
An = An-1 + An-2, A1 =1, A2 =2


'''

def fibo(n):
    if n == 1 or n == 2:
        return 1

    return fibo(n-1) + fibo(n-2)


print(fibo(6))



d = [0] * 10001

d[1] = 1
d[2] = 1

def fibo1(n):
    

    if d[n] != 0:
        return d[n]
    
    d[n] = fibo1(n -1) + fibo1(n -2)
    

    return d[n]

print(fibo1(6))