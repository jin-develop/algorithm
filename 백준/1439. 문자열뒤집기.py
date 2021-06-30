s = '0001100'
s = input()
n = list(s)

print(n)

aa = n[0]

result = []
for i in range(1, len(n)):

    if n[i] == n[i-1]:
        aa += n[i]
    else:
        result.append(aa)
        aa =n[i]
result.append(aa)

print(result)

print(len(result)//2)


