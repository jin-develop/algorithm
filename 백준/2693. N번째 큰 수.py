T = int(input())


for _ in range(T):
    array = list(map(int,input().split()))
    array.sort()

    print(array[-3])