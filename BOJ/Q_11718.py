# https://www.acmicpc.net/problem/11718 문제 제목 : 그대로 출력하기 , 언어 : Python, 날짜 : 2019-08-16, 결과 : 성공

while True:
    try:
        print(input())
    except EOFError:
        break
