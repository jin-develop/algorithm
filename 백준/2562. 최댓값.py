array = []

for _ in range(9):
    array.append(int(input()))

print(array)

max1 = max(array)

print(max1)
print(array.index(max1)+1)