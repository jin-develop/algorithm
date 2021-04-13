


while True:
    N = int(input())
    if N == 0:
        break
    array_org = []
    array = []
    for i in range(N):
        txt = input()
        array_org.append(txt)
        pp = txt.lower()
        array.append(pp)
    array_sorted = sorted(array)
    idx = array.index(array_sorted[0])
    print(array_org[idx])

