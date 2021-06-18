a, b = map(int,input().split())
d = [0] * 1000001
d[2] = True
d[3] = True
d[5] = True

if b > 5:
    for i in range(a, b+1):
        cnt = 0
        for j in range(1, i//2+1):
            if i % j == 0:
                cnt += 1
            
        if cnt == 1:
            d[i] = True

for i in range(a, b+1):
    
    if d[i] == True:
        print(i)


