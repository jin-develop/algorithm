t = int(input())
array = [input() for _ in range(t)]
result = 0


for i in array:
    new_array = []
    if len(i) == 1:
        result += 1
        continue

    if i[1] != i[0]:
        new_array.append(i[0])
        
    for j in range(1, len(i)):
        if i[j] != i[j-1]:
            new_array.append(i[j])
    if len(set(new_array)) == len(new_array):
        result += 1

print(result)


        