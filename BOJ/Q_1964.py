# https://www.acmicpc.net/problem/1964 문제 제목 : 오각형, 오각형, 오각형… , 언어 : Python, 날짜 : 2019-09-30, 결과 : 성공
N = int(input())
result = 5*N*(N+1)//2 - (N-1)*(N+1)
print(int(result%45678))
