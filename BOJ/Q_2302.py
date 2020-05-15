# https://www.acmicpc.net/problem/2302 문제 제목 : 극장 좌석 , 언어 : Python, 날짜 : 2020-05-15, 결과 : 성공 
"""
    회고:
    dp문제다. 솔직히 아직 dp는 너무 어렵게 느껴져서 실버 문제를 골랐는데, 뭔가 생각을 해보니 뭔 점화식이 만들어 졌다.
    그리고 그 형태가 피보나치 수열이랑 똑같다ㅋㅋ 오랜만에 순전히 혼자만의 힘으로 풀어본 dp문제다.
"""
import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
list_seat = []
last = 0
for _ in range(M):
    now = int(sys.stdin.readline())
    if now-last-1 > 0:
        list_seat.append(now-last-1)
    last = now
if last < N and N-last:
    list_seat.append(N-last)
result = 1
list_dp = [1,1]
for i in range(1, N):
    list_dp.append(list_dp[-1]+list_dp[-2])
for length in list_seat:
    result*=list_dp[length]
print(result)
