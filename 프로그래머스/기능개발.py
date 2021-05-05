


def solution(progresses, speeds):
    answer = []
    days = []
    for i in range(len(speeds)):
        day = (100 - progresses[i]) // speeds[i]
        day_rest = (100 - progresses[i]) % speeds[i]
        if day_rest != 0:
            days.append(day+1)
        else:
            days.append(day)
    rest = []
    rest.append(days[0])
    k = 0
    z = 1
    for j in range(1,len(days)):
        if days[j] <= rest[k]:
            days[j] = rest[k]
        else:
            rest.append(days[j])
            k += 1
            
    
    sor = sorted(set(days))
    
    for m in sor:
        answer.append(days.count(m))
    
    return answer