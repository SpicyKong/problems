# https://www.acmicpc.net/problem/11365 문제 제목 : !밀비 급일 , 언어 : Python, 날짜 : 2019-08-28, 결과 : 성공

import sys

while True:
    str_a = sys.stdin.readline()[:-1]
    if str_a=='END':
        break
    print(str_a[::-1])
    
"""
sys.stdin.readline() 이 함수는 을 주의해야한다..
"""
