T = int(input())
for _ in range(T):
    n, m = map(int,input().split())
    # N * N 은 배열크기 
    # M * M 은 M,M부터 M만큼 오른쪽 아래

    array = []
    for _ in range(n):
        array.append(list(map(int,input().split())))
    
    
    result = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            temp = 0
            for a in range(i, i+m):
                for b in range(j, j+m):
                    temp += array[a][b]
            if temp > result:
                result = temp

    print(result)
