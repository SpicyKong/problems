# https://www.acmicpc.net/problem/1712 문제 제목 : 손익분기점 , 언어 : Python, 날짜 : 20190804, 결과 : 성공

a, b, c = map(int, input().split())
if c-b>0:
    print(int(a/(c-b)) + 1)
else:
    print(-1)
