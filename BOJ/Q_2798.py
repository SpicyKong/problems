# https://www.acmicpc.net/problem/2798 문제 제목 : 블랙잭 , 언어 : Python, 날짜 : 2019-12-19, 결과 : 성공

import sys
N, M = map(int, sys.stdin.readline().split())
list_card = list(map(int, sys.stdin.readline().split()))
result = M+1
for i, num1 in enumerate(list_card):
        for j, num2 in enumerate(list_card):
            if not j==i:
                for k, num3 in enumerate(list_card):
                    if not k==i and not k==j:
                        re = M - (num1 + num2 + num3)
                        if re >= 0 and re < result:
                            result = re
                            res = [num1, num2, num3]
print(M-result)
