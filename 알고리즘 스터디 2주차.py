# 그리디 문제1
count = 0
N, K = input().split()
N = int(N)
K = int(K)
while N != 1:
    if N % K == 0:
        N /= K
        count += 1
    else:
        N -= 1
        count += 1
print(count)

# 이진탐색 문제
# N, M = map(int, input().split())
# list = list(map(int, input().split()))

# def count_list(H):
#     count_list = []
#     for i in list:
#         if i > H:
#             count_list.append(i - H)
#         else:
#             count_list.append(0)
        
#     return sum(count_list)

# def search(H, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1