T = int(input())

num = [] 
for test in range(T):
    array = list(map(int,input().split()))
    result = 0
    arr = []
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            for k in range(j+1, len(array)):
                result =str(array[i] + array[j] + array[k])
                arr.append(result)

    print(arr)

        


