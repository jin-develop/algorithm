cases = int(input())
for case in range(1, cases+1):
    N = int(input())
    # 너비는 10 고정
    array = ""
    for i in range(N):
        a, b = map(str,input().split())
        array += a * int(b)
    
    len_arr = len(array) // 10
    rest_arr = len(array) % 10
    
    
    for j in range(0,len_arr*10,10):
        print(array[j:j+10])
    if rest_arr != 0:
        print(array[len_arr*10:])
    
