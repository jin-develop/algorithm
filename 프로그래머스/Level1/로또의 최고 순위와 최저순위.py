

def solution(lottos, win_nums):
    answer = []
    rates = [6,6,5,4,3,2,1]
    zero = 0
    win = 0
    for i in range(len(lottos)):
        if lottos[i] == 0:
            zero += 1
        elif lottos[i] in win_nums:
            win += 1
    
    answer.append(rates[win+zero])
    answer.append(rates[win])
    return answer