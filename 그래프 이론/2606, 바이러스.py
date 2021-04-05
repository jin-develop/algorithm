'''
7
6
1 2
2 3
1 5
5 2
5 6
4 7
'''

N = int(input())
T = int(input())
gra = [[] for _ in range(N+1)]

for _ in range(T):
    a, b = map(int,input().split())
    gra[a].append(b)
    gra[b].append(a)

def dfs(v, gra):
    visited[v] = True
    for i in gra[v]:
        if visited[i] != True:
            dfs(i, gra)

print(gra)
visited = [0] * (N +1)
dfs(1, gra)
print(visited)
print(visited.count(True) - 1)