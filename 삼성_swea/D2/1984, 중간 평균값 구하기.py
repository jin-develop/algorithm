T = int(input())

for _ in range(T):
    
    array = list((map(int,input().split())))
    array.sort()
    
    array.pop()
    
    del array[0]
    print(round(sum(array)/len(array)))