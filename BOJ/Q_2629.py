# https://www.acmicpc.net/problem/2629 문제 제목 : 양팔저울 , 언어 : Python, 날짜 : 2020-02-25, 결과 : 성공
"""
  회고:
  나는 DP를 풀때 메모이제이션을 어떻게 할지에 대해 공부를 해야할것 같다. 정말 감이 안잡힌다.
  심지어 이 문제는 정올 초등부 문제인데..ㅠㅠ 세상에는 훌륭한 사람이 너무 많은것 같다.
"""
import sys

N = int(sys.stdin.readline())
list_weight = list(map(int, sys.stdin.readline().split()))+[0,0,0,0,0]
M = int(sys.stdin.readline())
list_ball = list(map(int, sys.stdin.readline().split()))

list_visit = [[0]*(30 * 500 + 1) for _ in range(30 + 1)]

def searching(count, weight):
    global N, list_visit, list_weight
    if count > N:
        return
    if list_visit[count][weight]:
        return
    list_visit[count][weight] = 1

    searching(count + 1, weight + list_weight[count])
    searching(count + 1, weight)
    searching(count + 1, abs(weight - list_weight[count]))

searching(0,0)
for i in range(M):
    if list_ball[i] <= 15000 and list_visit[N][list_ball[i]]:
        print('Y', end = '')
    else:
        print('N', end = '')
    if not i == M-1:
        print('',end=' ')
    
#print(list_visit[N])
#[print(a) for a in list_visit]
