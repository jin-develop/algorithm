Txt = input()

N = sorted(Txt)
many = 0
for i in N:
    for j in range(10):
        if i == str(j):
            many += 1
            break



number = N[:many]
str_list = N[many:]

num = 0
for i in range(len(number)):
    num += int(number[i])

for j in str_list:
    print(j,end='')
print(num)

