A,B,V = map(int,input().split())

day = 0
height = 0

while True:
    height += A
    day += 1
    if height >= V:
        break
    height -= B

print(day)

# 시간초과