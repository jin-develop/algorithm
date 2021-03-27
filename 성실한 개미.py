d_xy = [1, 1]
x, y = 1, 1
array = []

for _ in range(10):
    array.append(list(map(int,input().split())))

# 개미는 1,1 에서 시작

while True:
    if array[y][x] == 2:
        break
    array[y][x] = 9
    
    ny = y + d_xy[0]
    nx = x + d_xy[1]

    if array[y][nx] != 1:
        x = nx
        continue
    elif array[ny][x] != 1:
        y = ny
        continue

for k in array:
    for l in k:
        print(l, end=' ')
    print()
