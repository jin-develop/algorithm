a = int(input())
arr1 = input().split()
print(arr1)
x, y = 1, 1
default_arr = ['L', 'R', 'U','D']
dy_arr = [-1, 1, 0, 0]
dx_arr = [0, 0, -1, 1]


for i in arr1:
    

    for j in range(len(default_arr)):
        if i == default_arr[j]:
            nx = x + dx_arr[j]
            ny = y + dy_arr[j]
    
    if nx < 1 or ny < 1 or nx > a or ny > a:
        continue
    
    x, y = nx, ny
print (x, y)