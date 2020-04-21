# https://www.acmicpc.net/problem/5214 문제 제목 : 환승 , 언어 : Python, 날짜 : 2020-04-21, 결과 : 성공
"""
    이 문제에서 서술하는 하이퍼 튜브의 특성상 메모리가 초과할것 같았다. 생각을 해보는데도 도저히 떠오르지 않아서 결국 게시판을 참고하고 나서야 풀 수 있었다.
    역만 정점으로 두는것이 아니라 하이퍼 튜브또한 정점으로 두고 풀었다. 이렇게 되면 하이퍼 튜브가 추가될때마다 중복되어 표현되는 간선의 정보를 하나의 정점에서 표현할 수 있게 된다.
    지금까지 이렇게 생각을 해 본적이 없는데 되게 독특하고 좋은 접근법인것 같다. 근데 풀면서 한가지 실수 했던 부분이 있는데 하이퍼 튜브인 경우에 중복방문을 허락해준 점이다. 지금 생각해보니 멍청한 아이디어였지만
    문제를 풀때까지만 해도 와 이게 핵심 아이디어네 하면서 풀었다. 근데 생각해보니깐 내가 틀렸었다. 중복방문을 안해도 항상 최소값을 구할 수 있다. 멍청했다.

    오늘 코포 DIV3가 있다. 목표는 번역기 없이 abc 3솔 + 아무문제 +1솔 해서 총 4솔하고 싶다. 지금 코포 상황을 보면 쭉쭉 떨어지고만 있는데
    이제 어느정도 수렴할때가 된것같다. 열심히 해봐야겠다.

"""

import sys
from collections import deque
N, K, M = map(int, sys.stdin.readline().split())
list_map = [[] for _ in range(N + M+1)]
list_visit = [0]*(N + M+1)
for i in range(1,M+1):
    list_a = list(map(int, sys.stdin.readline().split()))
    list_map[N+i] = list_a
    for node in list_a:
        list_map[node].append(N+i)

list_queue = deque()
list_queue.append([1,1])
result = -1
while list_queue:
    now_node, now_count = list_queue.popleft()
    if now_node == N:
        result = now_count
        break
    for next_node in list_map[now_node]:
        if not list_visit[next_node] and next_node <= N:
            list_queue.append([next_node, now_count+1])
            list_visit[next_node] = 1
        elif not list_visit[next_node] and next_node > N:
            list_queue.append([next_node, now_count])
            list_visit[next_node] = 1
print(result)
