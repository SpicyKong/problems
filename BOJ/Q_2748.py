# https://www.acmicpc.net/problem/2748 문제 제목 : 피보나치 수 2 , 언어 : Python, 날짜 : 2019-10-14, 결과 : 성공
# 캡틴 이다솜 웰케 안풀리지..
import sys
dp =[0,1]
N = int(sys.stdin.readline())
if N==0:
    print(0)
else:
    i = 1
    while not N == i:
        dp.append(dp[i]+dp[i-1])
        i+=1
print(dp[-1])
