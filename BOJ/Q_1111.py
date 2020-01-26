# https://www.acmicpc.net/problem/1111 문제 제목 : IQ Test , 언어 : Python, 날짜 : 2020-01-26, 결과 : 실패
# 왜 안될까

import sys
N = int(sys.stdin.readline())
list_nums = list(map(int, sys.stdin.readline().split()))
list_save = list(list_nums)
list_result = []

def confirm(list_a, a, b, N):
    value = True
    for i in range(N-1):
        if not list_a[i+1] == list_a[i] * a + b:
            value = False
            break
    return value

if N >= 3:
    for i in range(10000):

        a_p = (list_nums[1] - i)//list_nums[0]
        a_n = (list_nums[1] + i)//list_nums[0]
        if list_nums[2] == a_p*list_nums[1] + i and confirm(list_nums, a_p, i, N):
            if not list_result:
                list_result.append(list_nums[-1]*a_p + i)
            elif not list_result[-1] == list_nums[-1]*a_p + i:
                list_result.append(list_nums[-1]*a_p + i)

        if list_nums[2] == a_n*list_nums[1] - i and confirm(list_nums, a_n, i * (-1), N):
            if not list_result:
                list_result.append(list_nums[-1]*a_n + i)
            elif not list_result[-1] == list_nums[-1]*a_p + i:
                list_result.append(list_nums[-1]*a_n + i)
    if list_result:
        if len(list_result) == 1:
            print(list_result[0])
        else:
            print('A')
    else:
        print('B')
else:
    if N == 1:
        print('A')
    elif N == 2:
        if list_nums[0] == list_nums[1]:
            print(list_nums[1])
        else:
            print('A')
