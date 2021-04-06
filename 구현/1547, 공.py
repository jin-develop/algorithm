array = [0, 1, 2, 3]

T = int(input())
for test in range(T):
    a, b = map(int,input().split())

    array[a], array[b] = array[b], array[a]
print(array.index(1))

