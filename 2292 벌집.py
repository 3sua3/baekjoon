N = int(input())
n = 1
if N == 1:
    print(1)
else:
    while True:
        number_one = n ** 3 - (n-1) ** 3
        number_two = (n + 1) ** 3 - n ** 3
        if number_one < N and number_two >= N:
            print(n + 1)
            break
        else:
            n += 1

    