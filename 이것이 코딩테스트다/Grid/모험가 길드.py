N = int(input())
array = list(map(int,input().split()))

array.sort()
result = 0
num = 0
for i in array:

    num += 1
    if num >= i:
        result += 1
        num = 0

print(result)


