N = input()

orgin = N

if int(N) < 10:
    N = '0'+N
cnt = 0

while True:
    first = N[-1]
    second = str(int(N[0])+int(N[1]))[-1]
    New_N = first + second
    cnt += 1
    if int(orgin) == int(New_N):
        break
    N = New_N


print(cnt)