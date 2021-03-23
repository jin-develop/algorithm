rest, b = map(int,input().split())
c= 0
while True:
    if rest % b ==0:
        rest = rest//5
        c +=1
    else:
        rest = rest -1
        c += 1
    if rest <= 1:
        break
        
print(c)