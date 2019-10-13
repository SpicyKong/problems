# https://www.acmicpc.net/problem/1660 문제 제목 : 캡틴 이다솜 , 언어 : Python, 날짜 : 2019-10-13, 결과 : 실패
# 틀린 이유 : dp로 풀어야 했는데 그리디알고리즘을 사용했다.
#             고쳐야하는데 낼모레가 모의고사다..
import sys

N = int(sys.stdin.readline())
need_list = [0,1]
dp_list = [1]*(N+2)

n=2
count = 0
while need_list[n-1] < N:
    need_list.append(need_list[-1] + n*(n+1)//2)
    n+=1
print(need_list)
"""
while N:
    if need_list[n-1] < N:
        need_list.append(need_list[-1] + n*(n+1)//2)
        n+=1
    else:
        while need_list[n-1] > N:
            n-=1
        N-=need_list[n-1]
        count += 1
"""
print(count)

"""
N = int(sys.stdin.readline())
need_list = [0,1]# + [0]*(N-1)
n=2
count = 0
while N:
    if need_list[n-1] < N:
        need_list.append(need_list[-1] + n*(n+1)//2)
        n+=1
    else:
        while need_list[n-1] > N:
            n-=1
        N-=need_list[n-1]
        count += 1
print(count)
1 4 10 20

1 1+2 1+2+3 1+2+3+4
1 1+3 1+3+6 1+3+6+10
dp[n] = dp[n-1] + n(n+1)/2 

"""
