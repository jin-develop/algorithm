n = int(input())
lst = []
for _ in range(n):
    name, d, m, y = input().rstrip().split()
    if len(m) == 1:
        m = '0' +m
    if len(d) == 1:
        d = '0'+d
    lst.append((name,y+m+d))
print(lst)


lst.sort(key=lambda x:int(x[1]))
print(lst[-1][0])
print(lst[0][0])

