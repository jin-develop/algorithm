
# heap을 사용해야 효율성을 통과하는데 
# 난 사용하지 않아 효율성은 0점


def solution(scoville, K):
    
    cnt = 0 
    while True:
        scoville.sort()
        if scoville[0] >= K:
            return cnt
        if len(scoville) == 1:
            if scoville[0] >= K:
                return cnt
            else:
                return -1
        elif len(scoville) == 2:
            if scoville[0] + scoville[1] * 2>= K:
                cnt += 1
                return cnt
            else:
                return -1
        else:
            cnt += 1
            new1 = scoville[0] + scoville[1] * 2
            del scoville[0]
            del scoville[0]
            scoville.append(new1)