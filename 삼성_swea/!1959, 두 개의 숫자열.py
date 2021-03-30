cases = int(input())
for case in range(1, cases+1):
    N, M = map(int,input().split())
    N_list = list(map(int,input().split()))
    M_list = list(map(int,input().split()))

    print(N_list)
    print(M_list)

    if M > N:
        N, M = M, N
        N_list, M_list = M_list, N_list

    total = []
    
    for i in range(M-N+1):
        result = 0
        # array = M_list[i:i+N]
        print(N_list)

        print('array', array)

        for j in range(N):
            times = N_list[j] * array[j]
            result += times
        total.append(result)

    print('total', total)

    # max1 = max(total)
    # print("#{} {}".format(case, max1))