# https://www.acmicpc.net/problem/1924 문제 제목 : 2007년 , 언어 : Python, 날짜 : 2019-11-26, 결과 : 성공

import sys

M, D = map(int, sys.stdin.readline().split())
list_date = [31,28,31,30,31,30,31,31,30,31,30,31]
day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
sum_date = sum(list_date[0:M-1])
sum_date += D
print(day[sum_date%7 - 1])
