N = int(input())

for _ in range(N):
    array1 = list(map(int,input().split()))
    T = array1[0]
    array2 = array1[1:]
    

    avg_array2 = sum(array2) / T
    cnt = 0

    for i in range(T):
        if array2[i] > avg_array2:
            cnt += 1
    avg = format((cnt/T) * 100, '.3f')
    print(str(avg) + '%')



