A, P = map(int,input().split())

array = []

while True:
    array.append(A)
    A_array = list(map(int,str(A)))
    result = 0
    for i in A_array:
        result = result + i ** P
    
    A = result

    if A in array:
        break

idx = array.index(A)

print(idx )
