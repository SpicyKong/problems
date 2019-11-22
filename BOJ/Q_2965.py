# https://www.acmicpc.net/problem/2965 문제 제목 : 캥거루 세마리 , 언어 : Python, 날짜 : 2019-11-22, 결과 : 성공
# 오늘도 대학 면접이있어서 갔다오느냐 좋은 문제를 못풀었다..
import sys

a,b,c = map(int, sys.stdin.readline().split())

if b - a> c - b:
    print(b-a-1)
else:
    print(c-b-1)
