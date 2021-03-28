money_cases = [50000,10000,5000,1000,500,100,50,10]

T = int(input())

for case in range(T):
    M = int(input())
    arr = []

    for money in money_cases:
        rest_n = M // money
        rest_money = M % money
        arr.append(rest_n)
        M = rest_money
    
    print("#{}".format(case+1))
    for i in arr:
        print(i, end=' ')
    print()
