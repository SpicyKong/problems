# https://www.acmicpc.net/problem/1456 문제 제목 : 거의 소수 , 언어 : Python, 날짜 : 2020-01-12, 결과 : 성공

import sys

A, B = map(int, sys.stdin.readline().split())
list_check = [0] * (int(B**0.5) + 1)
list_prime = []
list_check[0] = 1
list_check[1] = 1
count = 0
for i in range(1, int(B**0.5) + 1):
    if not i == 2 and (i%2 == 0 or i == 1):
        pass
    elif not list_check[i]:
        list_prime.append(i)
        n = 2
        while True:
            num = i * n
            if num > int(B**0.5):
                break
            list_check[num] = 1
            n += 1
            
for a in list_prime:
    n=2
    while True:
        num_a = a ** n
        if A <= num_a <= B:
            count+=1
        elif num_a > B:
            break
        n+=1
print(count)

"""
9
6


"""

