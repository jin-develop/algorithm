from itertools import combinations

def solution(orders, course):
    answer = []
    k = ''
    for i in orders:
        k += i
        
    k1 = list(k)
    k2 = sorted(set(k1))
    
    idx = []
    
    for z in course:
        list1 = list(combinations(k2, z))
        
        for j in range(len(list1)):
            qq = 0
            for l in range(len(orders)):
                ee = 0
                for oo in range(z):
                    if list1[j][oo] in orders[l]:
                        ee += 1
                if ee >= z:
                    qq += 1
                    
            if qq >= 2:
                idx.append(list1[j])
    print(idx)
    
    return answer