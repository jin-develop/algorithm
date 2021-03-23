# a = arr1수, b = 더하는 수, c = 인덱스 세번까지
a, b, c = map(int,input().split())
arr1 = list(map(int,input().split()))

arr1.sort()
result, j = 0, 0

print(arr1)
for i in range(1, b+1):
    j += 1
    if j > c:
        result += arr1[a-2]
        j = 0
        continue
    result += arr1[a-1]

print(result)
    

