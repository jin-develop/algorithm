array = [0,1,2,3,4,5,6,7,8]

n = list(map(int,input()))


for i in range(len(n)):
    if n[i] == 9:
        n[i] = 6
num_list = []

for j in array:
    if j == 6:
        if n.count(j) % 2 != 0:
            num = n.count(j)//2 + 1
        else:
            num = n.count(j) //2
        num_list.append(num)
    else:
        num = n.count(j)
        num_list.append(num)

print(max(num_list))
