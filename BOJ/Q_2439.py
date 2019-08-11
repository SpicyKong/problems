# https://www.acmicpc.net/problem/2439 문제 제목 : 별 찍기 - 2 , 언어 : Python, 날짜 : 2019-08-11, 결과 : 성공

b = int(input())
[print(' '*(b-a)+'*'*(a)) for a in range(1,b+1)]
