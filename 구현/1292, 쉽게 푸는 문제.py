a, b = map(int,input().split())
array = ''
for i in range(1, 46):
    array += str(i)*i

num = array[a-1:b]
result = 0

for j in num:
    result += int(j)

print(result)
print(type(result))