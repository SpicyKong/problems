# https://www.acmicpc.net/problem/2033 문제 제목 : 반올림 , 언어 : Python, 날짜 : 2020-01-03, 결과 : 실패
# 오늘은 하루종일 밖이라 코딩을 못한다..
# 왜 스트링으로 푼건 틀리는지 모르겟다. 반례도 못찾겠다...
import sys
from collections import deque
N = deque(sys.stdin.readline()[:-1])#list(map(int, list(sys.stdin.readline())))
len_N = len(N)
lesser = 10
point = 2
def re_new(len_list_a, list_a):
    list_a = deque(list_a)
    for i in range(1, len_list_a+1):
        if i == len_list_a:
            if int(list_a[len_list_a - i]) >= 10:
                list_a[len_list_a - i] = str(int(list_a[len_list_a - i]) - 10)
                list_a.appendleft('1')
                len_list_a +=1
            return len_list_a , list_a
        #print("test :",len_list_a - i)
        if int(list_a[len_list_a - i]) >= 10:
            list_a[len_list_a - i - 1] = str(int(list_a[len_list_a - i - 1]) + 1)
            list_a[len_list_a - i] = str(int(list_a[len_list_a - i]) - 10)
        #2 -1 -1


while int("".join(N)) > lesser:
    if int(N[len_N - point + 1]) >= 5:
        N[len_N - point + 1] = '0'
        N[len_N - point] = str(int(N[len_N - point]) + 1)
    elif int(N[len_N - point + 1]) < 5:
        N[len_N - point + 1] = '0'
    point+=1
    lesser*=10
    len_N, N = re_new(len_N, N)
print("".join(N))


# https://www.acmicpc.net/problem/2033 문제 제목 : 반올림 , 언어 : Python, 날짜 : 2020-01-04, 결과 : 성공
import sys

N = int(sys.stdin.readline())
standard_point = 10
while N > standard_point:
    if N%standard_point >= 5*standard_point//10:
        N = N//standard_point * standard_point + standard_point
    else:
        N = N//standard_point * standard_point
    standard_point*=10
print(N)
