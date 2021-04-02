T = int(input())
for _ in range(T):
    Txt = list(map(str,input()))
    Txt_reverse = Txt[::-1]

    if Txt ==Txt_reverse:
        print(1)
    else:
        print(0)