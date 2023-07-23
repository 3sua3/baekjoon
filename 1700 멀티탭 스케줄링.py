N, K = map(int, input().split())
list = list(map(int, input().split()))
count = 1
tab_list = []
for n, i in enumerate(list):
    if i not in tab_list and count <= N:
        tab_list.append(i)
        count += 1
    elif i not in tab_list and count > N:
        tab_list.append(i)