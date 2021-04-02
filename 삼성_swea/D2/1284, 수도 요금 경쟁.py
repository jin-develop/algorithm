P, Q, R, S, W = map(int,input().split())

A_cost = P * W

B_cost = 0
if R >= W:
    B_cost = Q
else:
    B_cost = Q + S * (W - R)

if A_cost >= B_cost:
    print(B_cost)
else:
    print(A_cost)
