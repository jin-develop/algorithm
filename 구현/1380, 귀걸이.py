

# 0이 나오면 종료
test = 0
while True:
    n = int(input())
    if n == 0:
        break
    else:
        test += 1
    girl_arr = []
    for i in range(n):
        girl_arr.append(input())

    array = []
    for j in range(n*2 -1):
        a, b = input().split()
        array.append(int(a))
    idx = 0
    for k in range(1,n+1):
        if array.count(k) == 1:
            idx = k
            break
    
    print(test, girl_arr[idx-1])

  