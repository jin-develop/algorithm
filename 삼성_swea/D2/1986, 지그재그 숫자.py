T = int(input())

for _ in range(T):
    N = int(input())
    array = []
    for i in range(1, N +1):
        if i % 2 == 0:
            array.append(-i)
        else:
            array.append(i)

    print(sum(array))
