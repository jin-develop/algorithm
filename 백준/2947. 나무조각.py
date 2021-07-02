array = list(map(int,input().split()))
ans = [1,2,3,4,5]

while array != ans:
    if array[0] > array[1]:
        array[0], array[1] = array[1], array[0]
        print(*array)
    if array[1] > array[2]:
        array[1], array[2] = array[2], array[1]
        print(*array)
    if array[2] > array[3]:
        array[2], array[3] = array[3], array[2]
        print(*array)
    if array[3] > array[4]:
        array[3], array[4] = array[4], array[3]
        print(*array)
