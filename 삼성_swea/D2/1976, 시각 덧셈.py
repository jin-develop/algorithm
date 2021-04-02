T = int(input())
for case in range(T):
    a,b,c,d = map(int,input().split())

    new_hour = a + c
    new_min = b + d

    if new_min >= 60:
        new_min -= 60
        new_hour += 1
    
    if new_hour >= 13:
        new_hour -= 12

    print("#{} {} {}".format(case+1,new_hour,new_min))