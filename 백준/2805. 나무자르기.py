a, b = map(int,input().split())

array1 = list(map(int,input().split()))
max1 = max(array1)

while True:
    cnt = 0
    for i in array1:
        if i - max1 < 0:
            continue
        else:
            cnt += i - max1
    if b == cnt:
        break
    max1 -= 1
print(max1)