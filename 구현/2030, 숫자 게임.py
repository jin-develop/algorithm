T = int(input())
num_org = []
for w in range(T):
    array = list(map(int,input().split()))
    result1 = [] 
    for i in range(len(array)):
        for j in range(i, len(array)):
            for k in range(j, len(array)):
                result = array[i] + array[j] + array[k]
                result1.append(result)
        
    for z in range(len(result1)):
        
    num = max(result1)
    num_org.append(num)
    num1 = num[-1]



