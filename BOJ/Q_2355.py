# https://www.acmicpc.net/problem/2355 문제 제목 : 시그마 , 언어 : Python, 날짜 : 2019-10-16, 결과 : 성공
#아까 dp 문제를 건드려 봤는데 왜인지 dp문제는 진짜 접근조차 못하겠다..
import sys
a,b = map(int, sys.stdin.readline().split())
if a > b:
    s= a
    a = b
    b = s
n = b-a+1
print((b+a)*n//2)
