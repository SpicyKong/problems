# https://www.acmicpc.net/problem/14501 문제 제목 : 퇴사 , 언어 : Python, 날짜 : 2020-02-21, 결과 : 성공
"""
    회고:
    이 문제는 완탐을 돌려도 풀리는 문제라서 쉽게 해결할 수 있었다.
    문제는 DP공부를 해야하는데 짜다 보면 완탐이 되어버려서 쉬운 문제는 풀리지만
    보통의 문제라면 풀리지 않는다..
"""
import sys
list_cost = []
list_reward = []

def next_day(day, result):
    global list_cost, list_reward, N
    if N <= day:
        if day < N+1:
            return result
        else:
            return 0
    return max(next_day(day + 1, result), next_day(day+list_cost[day], result + list_reward[day]))
    
    

N = int(sys.stdin.readline())
for _ in range(N):
    cost, reward = map(int, sys.stdin.readline().split())
    list_cost.append(cost)
    list_reward.append(reward)
print(next_day(0,0))
