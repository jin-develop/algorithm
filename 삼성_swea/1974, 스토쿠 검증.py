
# 9 * 9 스도쿠
array = []
for _ in range(9):
    array.append(list(map(int,input().split())))

# 가로비교 새로비교
result = 0
for i in range(9):
    new_arr = []
    for j in range(9):
        new_arr.append(array[i][j])
    if len(set(new_arr)) != 9:
        result += 1
        break

for i in range(9):
    new_arr = []
    for j in range(9):
        new_arr.append(array[j][i])
    if len(set(new_arr)) != 9:
        result += 1
        break


if result == 0:
    print(1)
else:
    print(0)