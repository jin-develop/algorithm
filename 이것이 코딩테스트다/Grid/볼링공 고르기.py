N, M = map(int,input().split())

array = list(map(int,input().split()))

result = 0
for i in range(len(array)):
    for j in range(i,len(array)):
        if array[i] != array[j]:
            result += 1

print(result)