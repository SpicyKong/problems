# https://www.acmicpc.net/problem/11004 문제 제목 : K번째 수 , 언어 : Python, 날짜 : 2019-10-26, 결과 : 실패
# 이 문제는 질문글탭에 가보니 정렬문제가 아니라 선택 알고리즘에 관한 문제라고 한다
# 참고로 아래코드는 python3으로 제출시 시간초과, PyPy3로 제출시 메모리초과가 뜬다..


import sys

def qsorting(arr, len_arr):
    if len_arr<=1:
        return arr
    pivot = arr[len_arr//2]
    lesser, equal, bigger =[], [], []
    count_lesser, count_bigger = 0, 0
    for num in arr:
        if num > pivot:
            bigger.append(num)
            count_bigger+=1
        elif num < pivot:
            lesser.append(num)
            count_lesser+=1
        else:
            equal.append(num)

    return qsorting(lesser, count_lesser) + equal + qsorting(bigger, count_bigger)

N, K = map(int, sys.stdin.readline().split())
list_num = list(map(int, sys.stdin.readline().split()))
print(qsorting(list_num, N)[K-1])
