S = list(map(int,input()))

result = 0
for i in S:
    if result == 0:
        result += i
        continue

    if i == 0 or i == 1:
        result += i
    else:
        result *= i

print(result)


