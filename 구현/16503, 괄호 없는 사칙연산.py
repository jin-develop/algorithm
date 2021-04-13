array = list(input().split())

print(array)
result = []


array[0], array[2], array[4] = int(array[0]),int(array[2]),int(array[4])
def k(a,b, p):
    if p =='+':
        return a + b
    if p =='-':
        return a - b
    if p == '*':
        return a * b
    if p == '/':
        return int(abs(a / b))

re1 = k(k(array[0],array[2],array[1]), array[4], array[3])
re2 = k(k(array[2],array[4],array[3]), array[0], array[1])

print(re1, re2)
