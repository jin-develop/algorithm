N = int(input())
array1 = []
for i in range(N):
    OX = input()
    cnt = 0
    sum = 0
    for j in range(len(OX)):
        if OX[j] == 'O':
            sum +=1
        else:
            sum = 0
        cnt += sum
    print(cnt)