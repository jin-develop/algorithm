
'''
5
3 2 1 1 9 -> 8
3
3 5 7 -> 1

'''

N = int(input())
array = list(map(int,input().split()))

array.sort()

x = 1

for i in array:
    if x < i:
        break
    x += i
print(x)

    
