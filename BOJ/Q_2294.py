# https://www.acmicpc.net/problem/2294 문제 제목 : 동전 2 , 언어 : Python, 날짜 : 2019-12-20, 결과 : 실패
# 런타임에러가 어디서 나는걸까?
import sys
n, k = map(int, sys.stdin.readline().split())
list_a = sorted(set([int(sys.stdin.readline()) for _ in range(n)]))
list_dp = [0] * (k + 1)
count_index = 0
for i in range(list_a[0], k + 1):
    if i == list_a[count_index]:
        list_dp[i] = 1
        if n > count_index:
            count_index += 1
    else:
        try:
             list_dp[i] = min([list_dp[i - j] for j in list_a if i > j and not list_dp[i - j] == 0]) + 1

        except:
            pass

if list_dp[-1]:
    print(list_dp[-1])
else:
    print(-1)
"""

1 2 3 4 5 6 7 8 9


"""
