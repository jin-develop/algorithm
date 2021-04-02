n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int,input().split())))

indx = 1
for i in array:
    
    if i[0] < i[1]:
        print("#",indx, "<")
    elif i[0] == i[1]:
        print("#",indx, "=")
    else:
        print("#",indx, ">")

    indx += 1