def solution(priorities, location):
    answer = 0
    s = len(priorities)
    n = []
    
#     n에 처음의 순서와 priority를 집어넣기
    for i in range(len(priorities)):
        a = []
        a.append(priorities[i])
        a.append(i)
        n.append(a)
    m = []
    
    cnt = 0
    while n:
        cnt += 1
        idx = 0
        len_n = len(n)
        n = n * 2
        max2 = n[0]
        max1 = n[0][0]
        # 순서대로 최대값 구하기
        for i in range(len(n)):
            if n[i][0] > max1:
                max1 = n[i][0]
                max2 = n[i]
                idx = i
#         print(max1, max2, idx)

#         print(n)
        del n[idx]
        m.append(max2)
        
        n = n[idx:idx+len_n-1]
        
    # print(m)
    for k in range(len(m)):
        if m[k][1] == location:
            return k+1
    