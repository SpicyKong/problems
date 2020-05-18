# https://www.acmicpc.net/problem/1700 문제 제목 : 멀티탭 스케줄링 , 언어 : Python, 날짜 : 2020-05-18, 결과 : 성공
"""
    회고:
    나는 나중에 뽑을수록 높은 우선순위를 부여해 문제를 풀었다. 먼저 한번 입력값을 탐색해보며 현재수가 언제 다시 나오는지 기록하고 다시 안나온다면 100이 넘는 수로 초기화한다.
    그 후 문제상황을 그대로 구현한다.
    1) 현재 꽂혀있으면 다음번 언제 또 나오는지 확인하고 업데이트함.
    2) 남는 구멍이 있다면 구멍을 사용함.
    3) 빼야한다면, 가장 우선순위가 높은것을 빼주고 그 자리에 꽂음.
    을 반복했다.
    뭔가 이 문제 구현을 하다가 자꾸 꼬여서 그냥 모조리 하드코딩 해버렸다..

    오늘 계란초밥 만들어 먹었는데 맛있었다.
"""
import sys

N, K = map(int, sys.stdin.readline().split())
list_schedule = list(map(int, sys.stdin.readline().split()))
list_check = [111]*K
list_former = [111]*(K+1)
list_onoff = [-1]*(K+1)
for i in range(K):
    #print(list_check)
    if not list_former[list_schedule[i]] == 111:
        list_check[list_former[list_schedule[i]]] = i
    list_former[list_schedule[i]] = i

count = 0
onoff = N-1
nagari = 0
list_multi = [0]*(N)
save = [i for i in range(N)]
for i in range(K):
    if not list_onoff[list_schedule[i]] == -1:
        list_multi[list_onoff[list_schedule[i]]] = i
    elif onoff>-1 and list_onoff[list_schedule[i]] == -1:
        list_onoff[list_schedule[i]] = onoff
        list_multi[onoff] = i
        onoff -= 1
    else:
        #print(list_multi)
        nagari = max(save, key=lambda x:list_check[list_multi[x]])
        list_onoff[list_schedule[list_multi[nagari]]] = -1
        list_onoff[list_schedule[i]] = nagari
        count += 1
        list_multi[nagari] = i

print(count)
"""
2 10
2 3 1 2 3 1 3 2 2 3

1 4 3 2 5 4 3 2 5 3 4 2 3 4
"""
