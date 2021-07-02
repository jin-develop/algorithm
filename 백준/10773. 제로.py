array = [] 

for _ in range(5):
    array.append(list(input()))

print(array)
answer = "" 
for i in range(15):
    for j in range(5):
        try:
            answer += array[j][i]
        except:
            continue

print(answer)