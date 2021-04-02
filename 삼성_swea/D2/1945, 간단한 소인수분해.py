cases = int(input())
# N = 2 * 3* 5 * 7 * 11
numbers = [2,3,5,7,11]

for case in range(1, cases+1):
    N = int(input())
    array = []
    for i in numbers:
        result = 0
        while True:
            
            New = N / i
            rest = N % i

            if rest != 0:
                array.append(result)
                break
            N = New
            result += 1

    print("#{}".format(case), *array)

    