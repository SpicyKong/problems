# https://www.acmicpc.net/problem/2884 문제 제목 : 알람 시계 , 언어 : Python, 날짜 : 2019-08-31, 결과 : 성공

H, M = map(int, input().split())
M-= 45
if M < 0:
    H-=1
    M = 60 + M
if H < 0:
    H= 24 + H
print(H, M)
