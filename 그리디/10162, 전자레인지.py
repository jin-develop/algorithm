Txt = int(input())
T = Txt

array = [300, 60, 10]

result_array = []
for i in array:
    result = 0
    rest = T % i
    ans = T // i
    result_array.append(ans)
    T = rest

sum1 = 0
for j in range(len(result_array)):
    sum1 += array[j] * result_array[j]


if sum1 == Txt:
    print(*result_array)
else:
    print(-1)

