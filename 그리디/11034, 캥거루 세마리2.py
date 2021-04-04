# A < B < C
import sys
input1 = sys.stdin.readline().rstrip()

a, b, c = map(int, input1.split())


if b-a > c-a:
    print((b-a)-1)
else:
    print((c-b)-1)