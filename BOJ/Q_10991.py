# https://www.acmicpc.net/problem/10991 문제 제목 : 별 찍기 - 16 , 언어 : Python, 날짜 : 2019-10-31, 결과 : 성공
# 면접이 코앞이라.. ㅠㅠ
import sys
N = int(sys.stdin.readline())
[print(' '*(N-i-1) + '*' + ' *'*(i)) for i in range(N)]
