T = int(input())
array1 = []


for _ in range(T):
    txt = list(input().split())
    if txt[0] == 'push':
        array1.append(int(txt[1]))
    elif txt[0] == 'pop':
        if len(array1) == 0:
            print(-1)
        else:
            array1.pop()
    elif txt[0] == 'size':
        print(len(array1))
    elif txt[0] == 'empty':
        if len(array1) == 0:
            print(1)
        else: 
            print(0)
    elif txt[0] == 'top':
        if len(array1) == 0:
            print(-1)
        else:
            print(array1[-1])

