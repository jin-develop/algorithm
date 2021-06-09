times = 1
for _ in range(3):
    times *= int(input())
times = str(times)

for i in range(10):
    print(times.count(str(i)))