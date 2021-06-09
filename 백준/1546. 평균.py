N = int(input())
array1 = list(map(int,input().split()))

max1 = max(array1)


print( sum(array1)/max1 *100 / N)