N = int(input())
i = 1


if N <= 99:
    print(N)
else:
    cnt = 0
    i = 100
    while (i <= N):
        M = list(str(i))
        if int(M[0]) - int(M[1]) == int(M[1]) - int(M[2]):
            cnt += 1
        i += 1
    print(99 + cnt)
    
            
    
