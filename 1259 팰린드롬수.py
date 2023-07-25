while True:
    number = input()
    word = ''
    if number == '0':
        break
    for i in range(len(number) - 1, -1, -1):
        word += number[i]
    if word == str(number):
        print('yes')
    else:
        print('no')