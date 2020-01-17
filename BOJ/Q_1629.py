# https://www.acmicpc.net/problem/1629 문제 제목 : 곱셈 , 언어 : Python, 날짜 : 2020-01-17, 결과 : 성공
# 분할정복이라는 개념을 몰라서 맨 밑에있는 코드처럼 구현을 시도했었다.
# 간략하게 설명하자면 나머지의 패턴을 구해서 적은 연산을 하도록 했는데 시간초과가 났다..

import sys


def custom_pow(a, b, c):
    if b == 1:
        return a%c
    elif b%2 == 0:
        return ((custom_pow(a, b//2, c)%c)**2)%c
    return ((custom_pow(a, (b-1)//2, c)%c)**2*a)%c

A, B, C = map(int, sys.stdin.readline().split())

print(custom_pow(A,B,C))


####################################################### 실패 코드 ###############################################
A, B, C = map(int, sys.stdin.readline().split())
if B < 100:
    print(((A%C)**B) % C)
else:
    count = 0
    const_A = int(A)
    list_pattern = [A%C]
    while A % C == A:
        A*=const_A
        count += 1
    start = int(count)
    add = list_pattern.append
    add(A%C)
    while True:
        A *= const_A
        add(A % C)
        if list_pattern[0] == A % C:
            break
        count+=1
    index = (B - start)%(count - start + 2)
    print(list_pattern[index])
