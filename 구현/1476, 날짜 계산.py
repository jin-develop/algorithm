a, b, c = map(int,input().split())
x, y, z, i = 1,1,1,1

# a <= 15, b <= 28, c <= 19

while True:
    if x==a and y==b and z==c:
        break

    x +=1; y+=1; z+=1; i+=1

    if x >= 16: x = 1
    if y >= 29: y = 1
    if z >= 20: z = 1

print(i)
