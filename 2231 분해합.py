N = int(input())
for i in range(1, N):
    word = str(i)
    n = i
    for j in word:
        n += int(j)
    if n == N:
        print(i)
        break
else:
    print(0)