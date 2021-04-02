T = int(input())
N = int(input())

print('#{}'.format(T))
for i in range(N):
    if i == 0:
        print(1)
    elif i == 1:
        print("1 1")
    else:
        print('1', end=' ')
        print((str(i)+' ')*(i-1)+'1')
        