T = int(input())
array = [[0]*101 for _ in range(101)]


for _ in range(T):
    a, b= map(int,input().split())

    for i in range(a, a+10):
        for j in range(b, b+10):
            array[i][j] += 1
cnt = 0
for x in range(len(array)):
    for y in range(len(array[0])):
        
        if array[x][y] > 0:
            cnt += 1


print(cnt)

