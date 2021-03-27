n = 10

for i in range(1, n+1):
    if '3' in str(i):
        print('-', end=' ')
    elif '6' in str(i):
        print('-', end=' ')
    elif '9' in str(i):
        print('-', end=' ')
    else:
        print(i, end=' ')