N = int(input())
weight_list = [input().split() for _ in range(N)]

number_list = []
for i in weight_list:
    k = 0
    weight = int(i[0])
    height = int(i[1])
    for j in weight_list:
        compare_weight = int(j[0])
        compare_height = int(j[1])
        if weight < compare_weight and height < compare_height:
            k += 1
    number_list.append(k + 1)

print(*number_list)