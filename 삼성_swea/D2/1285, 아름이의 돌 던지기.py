N = int(input())
array = list(map(int,input().split()))

for i in range(len(array)):
    array[i] = abs(array[i])

print(array)
array.sort()
result = 1
for j in range(1, len(array)):
    if array[j] == array[0]:
        result += 1
    else:
        break
print(array[0], result)
    