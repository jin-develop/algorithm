New = int(input())
i = 1
num = []

while True:
    
    N = New * i
    list_N = list(map(int,str(N)))

    
    for j in list_N:
        num.append(j)

    N_set = set(num)
    

    if len(N_set) == 10:
        
        break

    i += 1

print(i * New)