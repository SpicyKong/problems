# https://www.acmicpc.net/problem/1019 문제 제목 : 책 페이지 , 언어 : Python, 날짜 : 2020-03-27, 결과 : 성공
"""
    회고:
    백준님의 풀이인 https://www.slideshare.net/Baekjoon/baekjoon-online-judge-1019 를 참고했다.
    엄청나다. 최근에 회고란에 회고가 아닌 다른분들의 풀이에 대해 감탄만 적는것 같다.
    위 풀이는 규칙을 만들어낸 후 답을 도출한다.
    10 11 12 13 14 15 16 17 18 19
    20 21 22 23 24 25 26 27 28 29
    ...
    80 81 82 83 84 85 86 87 88 89
    이런식으로 일의 자릿수를 맞춰주게 되면 카운팅하기가 매우 간단해진다. 1의 자리에 0~9인까지가 총 8세트 있다.
    이 원리를 이용해 답을 도출해내면 된다. 어떻게 이런생각을 할수있는건지 모르겠다.
    
"""
import sys

def add(num, digit):
    for n in str(num):
        list_digit[dict_num[n]]+=digit

N = int(sys.stdin.readline())
dict_num = {str(i):i for i in range(10)}
list_digit=[0]*10
start = 1
digit = 1
while start <= N:
    while not N%10 == 9 and start <= N:
        add(N,digit)
        N -= 1
    if N < start:
        break
    while not start%10 == 0 and start <= N:
        add(start,digit)
        start += 1
    start//=10
    N//=10
    for i in range(10):
        list_digit[i] += (N - start + 1)*digit
    digit*=10
    
print(*list_digit)
