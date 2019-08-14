# https://www.acmicpc.net/problem/2851 문제 제목 : 슈퍼 마리오 , 언어 : Python, 날짜 : 2019-08-14, 결과 : 성공

import sys
total_num = 0
last_num = 0
mode = 0
for _ in range(10):
    total_num += int(sys.stdin.readline())
    if mode == 0 and abs(total_num-100) > abs(last_num-100):
        mode=1
    if mode==0:
        last_num = total_num
print(last_num)
