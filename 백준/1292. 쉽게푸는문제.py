a, b = map(int,input().split())
array = []
n = len(array)

cnt =1
while n < b:
    
    for i in range(cnt):
        array.append(cnt)
    cnt += 1
    n = len(array)


k = array[a-1: b]

print(sum(k))