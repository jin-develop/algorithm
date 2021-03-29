cases = int(input())
days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

for case in range(1, cases+1):
    a,b,c,d = map(int,input().split())

    ckdl = c- a
    if ckdl == 0:
        print(d-b+1)
    else:
        result = 0
        news = days[a:c]
        for new in news:
            result += new
        result += d- b + 1
        print(result)