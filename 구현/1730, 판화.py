n = int(input())
graph = [['.'] * n for _ in range(n)]

# 위 아래 왼 오
# U    D  L  R
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 0, 0 시작

array = list(input())
array_idx = ['U','D','L','R']

x, y= 0, 0

first = array[0]

if first == "U" or first == "D":
    graph[0][0] = '|'
else:
    graph[0][0] = "+"

for i in array:
    idx = array_idx.index(i)
    
    if i == "U" or i == "D":
        
        nx = x + dx[idx]
        ny = y + dy[idx]

        if nx <= -1 or ny <= -1 or nx >= n or ny >= n:
            continue

        if graph[x][y] == '-':
            graph[x][y] = '+'
        
        graph[nx][ny] = '|'


    elif i == "L" or i == "R":
        nx = x + dx[idx]
        ny = y + dy[idx]

        if nx <= -1 or ny <= -1 or nx >= n or ny >= n:
            continue

        if graph[x][y] == '|':
            graph[x][y] = '+'

        
        graph[nx][ny] = '-'

    x, y = nx, ny

for i in graph:
    for j in i:
        print(j,end='')
    print()
    