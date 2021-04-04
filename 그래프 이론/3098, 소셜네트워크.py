R, C = map(int,input().split())

# s = 양, W = 늑대
array = [list(input()) for _ in range(R) ]

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
rkqt = True

for x in range(R):
    for y in range(C):
        if array[x][y] == 'W':
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx <= -1 or ny <= -1 or nx >= R or ny >= C:
                    continue
                if array[nx][ny] == "S":
                    rkqt = False
                    break
                else:
                    array[nx][ny] = "D"
    if rkqt == False:
        break       

if rkqt == False:
        print(0)
else:
    print(1)
    for i in array:
        print(''.join(i))
        



