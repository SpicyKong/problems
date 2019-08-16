# https://www.acmicpc.net/problem/1920 문제 제목 : 수 찾기 , 언어 : Python, 날짜 : 2019-08-16, 결과 : 성공

import sys

b = [list(map(int,sys.stdin.readline().split())) for _ in range(4)]
[print(1) if a in b[1] else print(0) for a in b[3]]
