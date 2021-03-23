# 열 a 행 b 형태
a, b = map(int,input().split())
arr1 = []
for i in range(a):
    arr2 = list(map(int,input().split()))
    arr1.append(arr2)

pick = []

for j in range(len(arr1)):
    arr1[j].sort()
    pick.append(arr1[j][0])

print(pick[-1])


# OR
'''
for i in range(n):
    data = list(map(int,input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)

'''
