N = int(input())
number_list = list(map(int, input().split()))
count = 0
for i in number_list:
    if i != 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            count += 1

print(count)
