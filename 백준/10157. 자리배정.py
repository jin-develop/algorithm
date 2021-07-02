a, b = 7, 6
idx = 11



array = [[0] * a for _ in range(b)]


# 위 오른 아래 왼
dx = [-1,0,1,0]
dy = [0,1,0,-1]
cnt = 1
x, y = b-1, 0
i = 0

while True:
    array[x][y] = cnt
    nx = x + dx[i]
    ny = y + dy[i]
    if cnt == a * b:
        break

    if  nx < 0 or nx > b-1 or ny < 0 or ny > a-1 or array[nx][ny] != 0:
        i += 1
        if i > 3:
            i = 0
        continue

    x, y = nx, ny
    cnt += 1
    
for aaa in array:
    print(aaa)


for q in range(len(array)):
    for p in range(len(array[0])):
        if array[q][p] == idx:
            print(q, p)
            x, y= q, p
            break

print(a - x -1  , b - y  - 1 )
# a = 7 b = 6        == x = 0 y = 6
# a = 6 b = 6           x = 0 y = 5
# a = 1 b = 1           x = 5 y = 0