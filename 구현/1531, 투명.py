


N, M = map(int,input().split())
array = []
graph = [[0]* 100 for _ in range(100)]
for _ in range(N):
    array.append(list(map(int,input().split())))


for j in array:
    for k in range(j[0], j[2]+1):
        for z in range(j[1], j[3]+1):
            graph[k-1][z-1] += 1
result = 0

# M보다 큰 값을 구해야함

for x in graph:
    for j in x:
        if j > M:
            result += 1


print(result)