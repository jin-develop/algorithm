a, b = map(int,input().split())
array1 = list(map(int,input().split()))
sum1 = []
for i in range(len(array1)-2):
    for j in range(i+1,len(array1)-1):
        for k in range(j+1, len(array1)):
            sum2 = array1[i] + array1[j] + array1[k]
            if b < sum2:
                continue
            sum1.append(sum2)

sum1.sort(reverse=True)
print(sum1[0])

        