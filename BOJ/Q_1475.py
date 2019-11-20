# https://www.acmicpc.net/problem/1475 문제 제목 : 방 번호 , 언어 : Python, 날짜 : 2019-11-20, 결과 : 성공

import sys
list_num = [0,0,0,0,0,0,0,0,0,0]
N = sys.stdin.readline()[:-1]

for i in N:
    if i == '6':
        i = '9'
    list_num[int(i)] += 1
list_num[9] = round(list_num[9]/2 + 0.49)

print(max(list_num))
