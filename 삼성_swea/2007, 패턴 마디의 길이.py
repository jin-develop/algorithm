T = int(input())

for t in range(T):
    Txt = input()

    pre_txt = ""
    cnt = 1
    while True:
        pre_txt = Txt[:cnt]
        if cnt == 11:
            break
        for i in range(cnt, len(Txt), cnt):
            if pre_txt != Txt[i: i+ cnt]:
                break
            else:
                