'''
3 3
1 2
2 3
1 3

5 4
2 1
2 3
4 3
4 5

'''

N, M= map(int,input().split())

visited = [0] * (N+1)
graph = [[] for _ in range(M+1)]

def dfs(i, cnt):
    visited[i] = True
    for v in graph[i]:
        if visited[v] == 0:
            cnt = dfs(v, cnt+1)
    return cnt


for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = dfs(1,0)
print(cnt)

