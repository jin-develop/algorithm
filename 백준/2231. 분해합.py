N = int(input())

cnt = 1
while 1:
    cnt_st = str(cnt)
    cnt_list = list(cnt_st)
    sum = cnt
    for i in range(len(cnt_st)):
        sum += int(cnt_st[i])

    if sum == N:
        print(cnt)
        break
    cnt += 1

    if cnt >1000000:
        print(0)
        break