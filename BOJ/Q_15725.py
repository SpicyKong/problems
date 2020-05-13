# https://www.acmicpc.net/problem/15725 문제 제목 : 다항함수의 미분 , 언어 : Python, 날짜 : 2020-05-13, 결과 : 성공
"""
    회고:
    내일 미적분 시험이라 백준에 미분이라고 검색했더니 이런 문제가 나왔다. 아니 근데 계속 틀렸다..ㅋㅋ
    내일 미적분 시험은 안틀려야겠다.
"""
import sys
polynomical = sys.stdin.readline().split('x')
if len(polynomical) == 1:
    print(0)
elif not polynomical[0]:
    print(1)
elif polynomical[0] == '-':
    print(-1)
elif polynomical[0] == '+':
    print(1)
elif polynomical[0][0] == '+':
    print(eval(polynomical[0][1:]))
else:
    print(eval(polynomical[0]))
