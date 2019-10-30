# https://www.acmicpc.net/problem/11399 문제 제목 : ATM , 언어 : Python, 날짜 : 2019-10-30, 결과 : 성공
# 최근 풀었던 퀵소트를 사용한 문제에서 고안한 퀵소트 방법:
# 인자로 리스트만 넘겨줄게 아니라 len()함수를 자제 하도록 해서 좀더 시간초과에서 유연해지기 위함
import sys

def quick_sort(arr, len_arr):
    if len_arr <= 0:
        return arr
    pivot = arr[len_arr//2]
    lesser, equal, larger = [], [], []
    count_lesser, count_larger = 0, 0
    for num in arr:
        if num > pivot:
            larger.append(num)
            count_larger+=1
        elif num < pivot:
            lesser.append(num)
            count_lesser+=1
        else:
            equal.append(num)
    return quick_sort(lesser, count_lesser) + equal + quick_sort(larger, count_larger)

N = int(sys.stdin.readline())
list_a = list(map(int, sys.stdin.readline().split()))
list_a = quick_sort(list_a, N)
sum_result = 0
for i in range(N):
    sum_result += list_a[i] * (N-i)
print(sum_result)
