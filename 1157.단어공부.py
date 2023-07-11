word = list(input().upper())
word_set = list(set(word))
max_number = 0
for i in word_set:
    number = 0
    for j in range(0, len(word)):
        if i == word[j]:
            number += 1
    if number > max_number:
        max_number = number
        max_word = i
    elif number == max_number and i != max_word:
        max_word = '?'
        
        
print(max_word)