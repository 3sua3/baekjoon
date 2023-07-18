N, M = zip(input().split())
line = [list(input()) for _ in range(N)]
w_line = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
b_line = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
score_list = []
n = 0
while n + 7 < N:
    for i in line:
        new_line = i[n:n + 7]
