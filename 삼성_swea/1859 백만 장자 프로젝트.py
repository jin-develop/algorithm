N = int(input())
for t in range(1, N+1):
    num = int(input())
    array = list(map(int,input().split()))

    array = array[::-1]
    result = 0
    max_rkqt = array[0]
    for i in range(1, len(array)):
        if max_rkqt > array[i]:
            result += max_rkqt - array[i]
        else:
            max_rkqt = array[i]

    print(result)