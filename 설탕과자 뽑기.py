h, w = map(int,input().split())
n = int(input())

array = [[0] * h for _ in range(w)]
dirc = []
for _ in range(n):
    list1 = list(map(int,input().split()))
    list1[2], list1[3] = list1[2] -1, list1[3] -1
    dirc.append(list1)

for i in dirc:
    len3 = i[0]
    direction = i[1]
    array[i[2]][i[3]] = 1
    if direction == 0:
        for k in range(len3):
            array[i[2]][i[3]+k] = 1
    elif direction == 1:
        for hor in range(len3):
            array[i[2]+hor][i[3]] = 1

for list2 in array:
    for list3 in list2:
        print(list3, end=' ')            
    print()
