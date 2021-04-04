N = int(input())
T = int(input())


array = [list(map(int,input().split())) for _ in range(T)]

visited = [0] * (N+1)

def dfs(v):
    global visited
    visited[v] = True
    for i in array:
        if v in i:
            for j in i:
                if visited[j] != True:
                    visited[j] = True
                    v = j

    return visited

print(dfs(1))