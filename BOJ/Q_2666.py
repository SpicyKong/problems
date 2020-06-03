# https://www.acmicpc.net/problem/2666 문제 제목 : 벽장문의 이동 , 언어 : Python, 날짜 : 2020-06-03, 결과 : 성공
"""
    회고:
    풀다가 도저히 모르겠어서 다른분이 메모이제이션을 어떤식으로 했는지 참고했다. 뭔가 중복되는 연산을 캐치해내는게 미숙하다..
    우선 이 문제는 초기에 주어진 두 개의 문이 열려있고 미는 방식으로 문이 열리기 때문에 하나의 문이 새로 열리면 기존의 한개의 문이 닫히게 된다.
    따라서 계속 2개의 문은 열려있다. 문제의 관건은 두개의 문중 어느 문을 열고 닫았을떄 나중에 이득이 되는지 찾아야 한다.
    내가 참고한 메모이제이션 방법은 오른쪽 방법을 참고했다. dp[현재 몇번째 스케줄인지][열린문1][열린문2]

    사실 메모이제이션을 다른분의 아이디어를 참고했기 떄문에 내가 푼 문제는 아니다. 다시 도전해봐야 겠다.
"""

import sys
def opendoor(opened, now):
    global num_schedule
    if num_schedule-1<now:
        return 0
    #print(now, opened)
    if not list_memo[now][opened[0]][opened[1]]==-1:
        return list_memo[now][opened[0]][opened[1]]
    list_memo[now][opened[0]][opened[1]] = min(abs(opened[0]-list_schedule[now])+opendoor([list_schedule[now], opened[1]], now+1), abs(opened[1]-list_schedule[now])+opendoor([opened[0], list_schedule[now]], now+1))
    return list_memo[now][opened[0]][opened[1]]

N = int(sys.stdin.readline())
opened = list(map(int, sys.stdin.readline().split()))
num_schedule = int(sys.stdin.readline())
list_schedule = [int(sys.stdin.readline()) for _ in range(num_schedule)]
list_memo = [[[-1]*(N+1) for i in range(N+1)] for _ in range(num_schedule+1)]
print(opendoor(opened, 0))
