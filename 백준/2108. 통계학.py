T = int(input())
array = []
for _ in range(T):
    array.append(int(input()))
array.sort()


len1 = len(array)
set1 = set(array)
cnt = []
for i in set1:
    cnt.append((i,array.count(i)))


print(round(sum(array)/len1))
print(array[len1//2])
print(max(cnt, key=lambda x : x[1]))
print(max(array) - min(array))
