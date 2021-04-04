array = [25, 10, 5, 1]

T = int(input())
for test in range(T):
    money = int(input())

    plist = []
    for i in array:
        rest_money = money % i
        ans_money = money // i

        money = rest_money
        plist.append(ans_money)

    print(*plist)    