# https://www.acmicpc.net/problem/1834 문제 제목 : 나머지와 몫이 같은 수 , 언어 : Python, 날짜 : 2019-11-05, 결과 : 성공
# ez ㅋㅋ ㅈㅅ
import sys
N = int(sys.stdin.readline())
r = 0
for i in range(1,N):
    r += N * i + i
print(r)
