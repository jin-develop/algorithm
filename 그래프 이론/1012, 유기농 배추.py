'''
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
'''
import sys
sys.setrecursionlimit(10000)

M, N, K = map(int,input().split())

graph = [[0] * M for _ in range(N)]
for _ in range(K):
    a, b = map(int,input().split())
    graph[b][a] = 1

for i in graph:
    print(*i) 

# 상하 좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x,y):
    graph[x][y] =0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx <= -1 or ny <= -1 or ny >= N or nx >= M:
            continue
        if graph[nx][ny] == 1:
            dfs(nx,ny)

cnt = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            dfs(i,j)
            cnt += 1
print(cnt)