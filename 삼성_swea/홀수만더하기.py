n = int(input())
array = []
for j in range(n):
    array.append(list(map(int,input().split())))

idex = 1
for i in array:
    result = 0
    for k in i:
        if k % 2 != 0:
            result += k
        
    print("#",idex, result)
    idex += 1
