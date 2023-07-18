N = int(input())
list = list(map(int, input().split()))
list.sort()
count = 0
for n, m in enumerate(list):
    for j in range(n + 1):
        count += list[j]
print(count)