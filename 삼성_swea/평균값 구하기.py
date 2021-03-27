n = int(input())
array = []

for _ in range(n):
    array.append(list(map(int,input().split())))

indx = 1
for i in array:
    array_sum = sum(i)
    
    print('#',indx, round(array_sum/len(i)))
    indx += 1