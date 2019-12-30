# https://www.acmicpc.net/problem/4948 문제 제목 : 베르트랑 공준 , 언어 : Python, 날짜 : 2019-12-30, 결과 : 성공

import sys

while True:
    list_sosu = [0]*2 + [1]*(123456*2-2)
    for i in range(2,int((123456*2 + 1)**0.5) + 1):
        n = 2
        while i * n < 123456*2:
            if list_sosu[i * n]:
                list_sosu[i * n] = 0
            n += 1
    input_num = int(sys.stdin.readline())
    if input_num == 0:
        break
    else:
        print(sum(list_sosu[input_num+1: input_num*2 + 1]))
