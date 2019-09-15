# https://www.acmicpc.net/problem/7576 문제 제목 : 토마토 , 언어 : Python, 날짜 : 2019-08-12, 결과 : 실패
# https://www.acmicpc.net/problem/7576 문제 제목 : 토마토 , 언어 : Python, 날짜 : 2019-09-15, 결과 : 성공

#   기존의 방법에서 불필요한 조건문을 없애서 확실히 실행시간 단축에 도움이 되긴 했는데
#   계속 하다보니 10% 지점에서 틀린다. 다시 수정해봐야 겠다.
# 2019.09.15 : BFS를 공부하고 다시 풀어보았다. 아, 그리고 큐를 구현할때 .pop(0) 사용은 지양해야 한다는 것을 알았다.
#              왜냐하면, pop()함수가 동작할 때 n > n-1, n-1 > n-2 ... 이런식으로 원소를 옮겨서 시간복잡도가 O(N)인 함수라고 한다.

#####################################################################################################
#
#      ver1 : 틀렸습니다. BFS를 배우기 전 코드
#
import sys
x,y =map(int, sys.stdin.readline().split())

list_tomato = [sys.stdin.readline().split() for _ in range(y)]
tomato = True
thereistomato = 0
count=0
while(tomato):
    thereistomato = 0
    for a,b in enumerate(list_tomato):
        for c,d in enumerate(b):
            #print("asdf")
            #print(d)
            if count%2==0 and d=='1':
                try:
                    if list_tomato[a-1][c] =='0':
                        list_tomato[a-1][c]='2'
                        if thereistomato==0:
                            thereistomato+=1
                except:
                    pass
                try:
                    if list_tomato[a+1][c] =='0':
                        list_tomato[a+1][c]='2'
                        if thereistomato==0:
                            thereistomato+=1
                except:
                    pass
                try:
                    if list_tomato[a][c-1] =='0':
                        list_tomato[a][c-1]='2'
                        if thereistomato==0:
                            thereistomato+=1
                except:
                    pass
                try:
                    if list_tomato[a][c+1] =='0':
                        list_tomato[a][c+1]='2'
                        if thereistomato==0:
                            thereistomato+=1
                except:
                    pass

            elif count%2==1 and d=='2':
                try:
                    if list_tomato[a-1][c] =='0':
                        list_tomato[a-1][c]='1'
                        if thereistomato==0:
                            thereistomato+=1
                except:
                    pass
                try:
                    if list_tomato[a+1][c] =='0':
                        list_tomato[a+1][c]='1'
                        if thereistomato==0:
                            thereistomato+=1
                except:
                    pass
                try:
                    if list_tomato[a][c-1] =='0':
                        list_tomato[a][c-1]='1'
                        if thereistomato==0:
                            thereistomato+=1
                except:
                    pass
                try:
                    if list_tomato[a][c+1] =='0':
                        list_tomato[a][c+1]='1'
                        if thereistomato==0:
                            thereistomato+=1
                except:
                    pass
    if thereistomato==0:
        break
    count+=1
asdf = 0
#[print(a) for a in list_tomato]
for a,b in enumerate(list_tomato):
    if '0' in b:
        print('-1')
        asdf =1
        break
if asdf==0:
    print(count)
    
 
#####################################################################################################
#
#      ver2 : 틀렸습니다. BFS를 적용한 코드. 하지만 불필요한 반복문이 너무 많아서 시간초과, 123라인의 큐를 적극활용하라는 조언을 얻음
#
from collections import deque
import sys

M, N = map(int, sys.stdin.readline().split())
list_tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] # 토마토 리스트
list_visit = [[0]*M for _ in range(N)] # 방문을 표시하기 위한 리스트
list_queue = deque() # 그냥 .pop(0) 을 쓰면 시간복잡도가 O(N)이 되므로 deque를 사용했습니다.
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
save_count = 0
count_q = 0
while True:
    count_queue = 0 #list_queue 의 원소의 개수를 저장하는 변수
    count_zero = 0 # 현재 토마토의 리스트에 있는 0의 개수를 저장하는 변수
    for y in range(N):
        for x in range(M):
            if list_tomato[y][x] == 1:
                for i in range(4):
                    ax = x + dx[i]
                    ay = y + dy[i]
                    if 0 <= ax < M and 0 <= ay < N:
                        if list_tomato[ay][ax] == 0 and list_visit[ay][ax]==0:
                            list_visit[ay][ax] = 1 # 방문 처리
                            list_queue.append([ay,ax]) # 방문 처리한 list_visit의 좌표를 큐에 저장
                            count_queue+=1
                            count_zero-=1
            elif list_tomato[y][x] == 0:
                count_zero += 1
    if count_queue == 0:
        break
    for i in range(count_queue):
        vy, vx = list_queue.popleft()
        list_tomato[vy][vx] = 1
    count_q+=1
if count_zero == 0:
    print(count_q)
else:
    print(-1)
#####################################################################################################
#
#      ver3 : 맞았습니다!
#
from collections import deque
import sys

def nextDay(queue1, queue2):
    global list_tomato, list_visit, dx, dy
    while queue1:
        y, x = queue1.popleft()
        list_tomato[y][x] = 1
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if 0 <= ax < M and 0 <= ay < N:
                if list_tomato[ay][ax] == 0 and list_visit[ay][ax]==0:
                    list_visit[ay][ax] = 1
                    queue2.append([ay,ax])
    
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
M, N = map(int, sys.stdin.readline().split())
list_tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
list_visit = [[0]*M for _ in range(N)]
list_queue1 = deque()
list_queue2 = deque()
for y in range(N):
    for x in range(M):
        if list_tomato[y][x] == 1:
            for i in range(4):
                ax = x + dx[i]
                ay = y + dy[i]
                if 0 <= ax < M and 0 <= ay < N:
                    if list_tomato[ay][ax] == 0 and list_visit[ay][ax]==0:
                        list_visit[ay][ax] = 1
                        list_queue1.append([ay,ax])

save_count = 0
count_q = 0
is_there_zero = 0
while list_queue1 or list_queue2:
    count_q+=1
    if list_queue1:
        nextDay(list_queue1, list_queue2)

    else:
        nextDay(list_queue2, list_queue1)
for y in range(N):
    for x in range(M):
        if list_tomato[y][x] == 0:
            is_there_zero = 1
            break

if is_there_zero:
    print(-1)
else:
    print(count_q)
