import itertools 



n = int(input())
ar2 = list(map(int,input().split()))

array = []

for i in range(1, n+1):
    array.append(i)


ar1 = list(itertools.permutations(array,n))


for j in range(len(ar1)):
    if list(ar1[j]) == ar2:
        if j == 0:
            print(-1)
            break
        else:
            print(*list(ar1[j-1]))
            break
