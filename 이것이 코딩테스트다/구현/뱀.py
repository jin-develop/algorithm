N = int(input())
K = int(input())
apple = []
for _ in range(K):
    apple.append(list(map(int,input().split())))

many = int(input())
direction = []
for _ in range(many):
    direction.append(list(map(str,input().split())))

graph = [[0] * N for _ in range(N)]

for i in apple:
    graph[i[0]-1][i[1]-1] = 1

print(graph)

count = 0
i = 0
# 우 하 좌 상
dx = [0,1,0,-1]
dy = [1,0,-1,0]
x, y = 0, 0
while True:
    nx = x + dx[i]
    ny = y + dy[i]
    count += 1
    if nx >= N or ny >= N or ny <= -1 or nx <= -1:
        break
    if graph[nx][ny] == 