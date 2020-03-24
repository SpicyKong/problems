# https://www.acmicpc.net/problem/1981 문제 제목 : 배열에서 이동 , 언어 : Python, 날짜 : 2020-02-13, 결과 : 실패
# 맞왜틀..

import sys
from collections import deque

N = int(sys.stdin.readline())
list_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
list_visit = [[0]*N for _ in range(N)] # 방문을 체크하는 동시에 방문을 했다면 [최소, 최대, 차]값을 저장하는 2차원 리스트입니다.

list_queue = deque([[0,0,list_map[0][0],list_map[0][0],207]]) # [x좌표, y좌표, 현재 최소값, 현재 최대값, 차]를 저장하고 BFS에 이용하는 큐입니다.
list_visit[0][0] = [list_map[0][0],list_map[0][0],201] # 방문을 체크할때 옆과같이 [최소, 최대, 차]값을 저장해 둡니다. 200이 문제에서 나올수있는 차의 최댓값이기 때문에 그보다 큰 201로 초기화.
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while list_queue:
    now_x, now_y, now_min, now_max, now = list_queue.popleft()
    print("=============")
    [print(a) for a in list_visit]
    for i in range(4):
        nx = now_x + dx[i]
        ny = now_y + dy[i]
        if 0 <= nx < N and 0 <= ny < N: # 리스트의 범위를 벗어 나지 않는다면
            nmin = min(now_min, list_map[ny][nx]) # 현재 최소값
            nmax = max(now_max, list_map[ny][nx]) # 현재 최대값
            if not list_visit[ny][nx]: # 이동하려는 칸이 방문한적이 없었다면
                list_visit[ny][nx] = [nmin, nmax, nmax-nmin] # 방문체크
                list_queue.append([nx, ny, nmin, nmax, nmax-nmin]) # 큐에 값을 넣어줌
            elif list_visit[ny][nx][2] > nmax - nmin: # 방문을 했었지만, 차의값을 줄일수있는 경로라면
                list_visit[ny][nx] = [nmin, nmax, nmax-nmin] # 방문체크된 값을 새롭게 저장
                list_queue.append([nx, ny, nmin, nmax, nmax-nmin]) # 큐에 값을 넣어줌
print(list_visit[N-1][N-1][2])





#####################################################################################################################
# https://www.acmicpc.net/problem/1981 문제 제목 : 배열에서 이동 , 언어 : Python, 날짜 : 2020-03-25, 결과 : 성공
"""
    회고:
    아마 이 문제를 구글에 검색해보면 아래 코드와 유사한 정답코드가 있을것이다. 나 역시 그분의 코드를 참고해서 작성했다.(거의 복사수준)
    내가 처음 실수했던 부분은 이 문제에서 이분탐색을 진행할때 이분탐색이라고 생각했던 코드가 이분탐색이 아니였다.
    처음 mid값은 (최고 + 최저)/2 의 몫이였지만 그다음 진행할때는 그렇지 않았다. 
    그리고 이 부분말고도 결정적인 실수는 right 값을 점점 늘려보며 bfs를 진행할때 먼저 나온답이 무조건 정답이라고 생각했던 부분이다.
    내가 생각한 반례는 아래와 같은데 아래 케이스는 8과 9만 거쳐서 (N-1,N-1)에 도달할수있지만
    내가 맨처음 생각한 방법에 의하면 right값을 1씩 늘려주며 탐색을 하므로 right값이 8이되면 더이상 늘어나지 않아
    9인 지점에 방문조차 할수없는 상황이 생긴다.

    P.S. 회고작성의 장점은 내가 틀린부분에 대해 생각할 기회를 준다는 점인것 같다.
    
    4
    8 8 8 8
    0 8 0 0
    8 9 8 8
    8 8 8 8
    ans : 1
"""

import sys
from collections import deque

def bfs(diff):
    list_visit = [[-1]*N for _ in range(N)]
    for k in list_num:
        list_queue = deque()
        if k <= list_map[0][0] <= k + diff:
            list_queue.append([0,0])
        while list_queue:
            now_x, now_y = list_queue.popleft()
            for i in range(4):
                nx = now_x + dx[i]
                ny = now_y + dy[i]
                if 0<=nx<N and 0<=ny<N:
                    if k <= list_map[ny][nx] <= k + diff and not list_visit[ny][nx] == k+1:
                        if ny == N-1 and nx == N-1:
                            return True
                        list_visit[ny][nx] = k + 1
                        list_queue.append([nx, ny])
    return False

def solve():
    start = 0
    end = max_value - min_value
    while start <= end:
        mid = (start + end)//2;
        print(mid)
        if bfs(mid):
            end = mid-1
        else:
            start = mid + 1
    return end + 1

N = int(sys.stdin.readline())
list_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
min_value = 201
max_value = -1
dx = [1,-1,0,0]
dy = [0,0,1,-1]
list_num = set([])
for y in range(N):
    for x in range(N):
        if list_map[y][x] > max_value:
            max_value = list_map[y][x]
        if list_map[y][x] < min_value:
            min_value = list_map[y][x]
        list_num.add(list_map[y][x])

mid_value = (max_value + min_value)//2
list_num = sorted(list(list_num))
len_num = len(list_num)
print(solve())


"""
4
8 8 8 8
0 8 0 0
8 9 8 8
8 8 8 8

5
7 1 7 7 7
7 1 7 7 7
7 7 7 7 7
7 7 7 7 7
7 7 7 7 7


2
2 1
2 3
5
7 7 3 6 8
1 7 2 5 5
4 7 7 7 3
8 0 2 7 4
4 3 0 7 7
2
2 1
2 3
4
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
5
4 3 3 5 5
3 9 9 9 9
3 9 2 2 3
4 9 1 9 2
5 4 3 9 0

5
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 10
0 0 0 10 200

7
1 1 1 7 1 1 1
1 5 1 6 1 1 1
1 5 1 5 1 4 1
1 5 1 4 1 5 1
1 5 1 3 1 6 1
1 5 1 2 1 8 1
1 5 1 0 1 9 1

8
1 1 1 3 1 1 1 2
3 3 1 3 1 2 1 2
1 1 1 1 1 2 1 2
3 3 3 3 3 3 1 2
1 1 1 3 3 2 1 2
1 2 1 1 1 1 1 2
1 3 3 3 3 2 2 2
1 1 1 1 1 1 1 1

8
0 1 2 3 4 5 6 7
1 1 2 3 4 5 6 7
2 2 2 3 4 5 6 7
3 3 3 3 4 5 6 7
4 4 4 4 4 5 6 7
5 5 5 5 5 5 6 7
6 6 6 6 6 6 6 7
7 7 7 7 7 7 7 7
"""

        
