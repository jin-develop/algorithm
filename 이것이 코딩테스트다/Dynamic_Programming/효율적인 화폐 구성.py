N, M = map(int,input().split())

array = [int(input()) for _ in range(N)]

d = [10001] * (M +1)

d[0] = 0

for i in range(n):
    for j in range(array[i], M+1):
        if d[j-array[i]] != 10001:
            d[j] = min(d[j], d[j-array[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])

    