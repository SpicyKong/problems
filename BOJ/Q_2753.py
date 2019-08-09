# https://www.acmicpc.net/problem/2753 문제 제목 : 윤년 , 언어 : Python, 날짜 : 2019-08-09, 결과 : 성공

num = int(input())
if num%4==0 and not num%100==0:
    print(1)
elif num%400==0:
    print(1)
else:
    print(0)

