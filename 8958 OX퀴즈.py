number = int(input())
quiz_list = [input() for _ in range(number)]
for i in quiz_list:
    i_list = list(i)
    count = 0
    for n, j in enumerate(i_list):
        if j == 'O':
            if i_list[n - 1] == 'X' or n == 0:
                w = 0
                while n + w <= len(i_list) -1 and i_list[n + w] == 'O':
                    w += 1
                sub_count = w * (w + 1) / 2
                count += sub_count
    print(int(count))
