N = list(map(int,input()))



N_len = len(N)

N_first = N[:N_len//2]
N_second = N[N_len//2:]

result_1, result_2 = 0, 0
for i in range(len(N_first)):
    result_1 += N_first[i]
    result_2 += N_second[i]

if result_1 == result_2:
    print("LUCKY")

else:
    print("READY")
