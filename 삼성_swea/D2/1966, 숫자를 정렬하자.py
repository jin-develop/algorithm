T = int(input())

for case in range(T):
    N = int(input())
    array = list(map(int,input().split()))

    array.sort()
    print("#{}".format(case+1), end=' ')
    for a in array:
        print(a, end=' ')
    print()