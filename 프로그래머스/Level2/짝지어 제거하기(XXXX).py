s = 'baabaa'

cnt = 0
    
while (cnt< 500000):
    org = s
    for i in range(0, len(s)-1):
        if s[i] == s[i+1]:
            org = org.replace(s[i],"",2)
            print(org)
            break
            
    if len(org) == 0:
        break
    s = org
    cnt += 1
    
if len(org) == 0:
    print(1)
else:
    print(0)


# 스택으로 문제풀기