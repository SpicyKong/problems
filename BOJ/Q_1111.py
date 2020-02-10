# https://www.acmicpc.net/problem/1111 문제 제목 : IQ Test , 언어 : Python, 날짜 : 2020-01-26, 결과 : 실패
# https://www.acmicpc.net/problem/1111 문제 제목 : IQ Test , 언어 : Python, 날짜 : 2020-02-10, 결과 : 성공
# 왜 안될까
# 다시 식세우고 해보니 바로 맞았다!

# 성공코드
import sys

N = int(sys.stdin.readline())
list_nums = list(map(int, sys.stdin.readline().split()))

"""
n1 = n1
n2 = n1*a + b
n3 = n2*a + b = (n1*a + b)*a + b

n3 - n2 = (n1*a + b)*a + b - n1*a - b
        = n1*a*a + a*b + b - n1*a - b
        = a(n1*a + b - n1)
        = a(n2 - n1)
(n3 - n2)/(n2 - n1) = a
"""
if N == 1:
    print('A')
elif N == 2:
    if list_nums[0] == list_nums[1]:
        print(list_nums[0])
    else:
        print('A')
else:
    if list_nums[1] - list_nums[0]:
        A = (list_nums[2] - list_nums[1])//(list_nums[1] - list_nums[0])
    else:
        A = 1
    B = list_nums[1] - list_nums[0]*A

    check = 0
    for i in range(N-1):
        if not list_nums[i+1] == list_nums[i]*A + B:
            check = 1
            break
    if check:
        print('B')
    else:
        print(list_nums[-1]*A + B)
    

################### 실패코드
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
