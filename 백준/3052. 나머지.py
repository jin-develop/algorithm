array1 = []
for _ in range(10):
    array1.append(int(input()) % 42)
cnt = 0
for i in range(len(array1)):
    if array1.count(array1[i]) == 1:
        cnt += 1

print(cnt)

