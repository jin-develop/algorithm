from collections import deque
N, K = map(int,input().split())

# N * N
array = []
for _ in range(N):
    array.append(list(map(int,input().split())))

'''
x, y 좌표가 있음
x는 아래로 y는 오른쪽으로 가야함
만약 밖으로 나가면 예외처리

'''

