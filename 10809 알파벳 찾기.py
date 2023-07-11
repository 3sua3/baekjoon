from string import ascii_lowercase

alphabet_list = list(ascii_lowercase)

word = list(input())

alphabet_number = []

for i in alphabet_list:
    number = 0
    for j in word:
        if i == j:
            number += 1
            numbertwo = word.index(j)
    if number == 0:
        numbertwo = -1
    alphabet_number.append(numbertwo)

print(*alphabet_number)