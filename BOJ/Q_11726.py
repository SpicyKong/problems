# https://www.acmicpc.net/problem/11726 문제 제목 : 2×n 타일링 , 언어 : Python, 날짜 : 2019-10-11, 결과 : 성공

import sys
list_dp = [1,2]
n = int(sys.stdin.readline())
if 2 < n:
    for _ in range(n-2):
        list_dp.append(list_dp[-1]+list_dp[-2])
print(list_dp[n-1]%10007)
