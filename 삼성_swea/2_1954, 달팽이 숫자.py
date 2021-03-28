cases = int(input())
for case in range(1, cases+1):
    N = int(input())
    
    a = [[0] * N for _ in range(N)]

    #오른, 아래, 왼, 위
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    x = y = 0
    i, cnt = 0, 1

    while True:
        a[x][y] = cnt
        nx = x + dx[i] # 0 0 1 2 2 2 1 1
        ny = y + dy[i] # 1 2 2 2 1 0 0 1
        if nx >= N or ny >= N or nx <= -1 or ny <= -1 or a[x][y] != 0:
            i += 1
            if i >= 4:
                i -= 4
        else:

            cnt += 1
            x, y = nx, ny
            
            if cnt == N**2:
                a[x][y] == cnt
                break

    for i in a:
        for j in i:
            print(j, end=" ")
            print()
