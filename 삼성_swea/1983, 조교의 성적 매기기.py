rate = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
T = int(input())

for l in range(T):
    N, K = map(int,input().split())
    array = []
    for i in range(N):
        
        a, b, c = map(int,input().split())
        total = a * 0.35 + b * 0.45 + c * 0.2
        if i == K-1:
            K_total = total
        array.append(total)
    array.sort(reverse=True)
    find_K = array.index(K_total)

    N_rate = N / 10
    # 만약 2명씩이라면, 01 - A+
    find_K = int(find_K // N_rate)

    print("#{} {}".format(l+1, rate[find_K]))





        

    
