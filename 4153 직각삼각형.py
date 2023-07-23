while True:
    number_list = list(map(int, input().split()))
    number_list.sort()
    a = number_list[0]
    b = number_list[1]
    c = number_list[2]
    if a == 0 and b == 0 and c == 0:
        break
    if c ** 2 == (a ** 2 + b ** 2):
        print('right')
    else:
        print('wrong')
