# 문제 제목 : 컬러볼 , 언어 : Python, 날짜 : 20190731, 결과 : 시간초과


num = int(input())
list_color = []
list_input = []
list_seq = []
for a in range(num):
    input_data = input().split()   
    input_data[0] = int(input_data[0])
    input_data[1] = int(input_data[1])
    if not input_data[0] in list_color:
        list_color.append(input_data[0])
        list_input.append([])
    color_index = list_color.index(input_data[0])
    list_input[color_index].append(input_data[1])
    list_seq.append([color_index,len(list_input[color_index])-1])

for a in range(num):
    asum = 0
    list_color_find = [b for b in range(len(list_color)) if not b == list_seq[a][0]] 
    for c in list_color_find:
        asum += sum([d for d in list_input[c] if d < list_input[list_seq[a][0]][list_seq[a][1]]])
    print(asum)

#___________________________________________________________________________________________________________
# 밑은 다시 작성한 버전, 시간초과..

num = int(input())
#list_a = [input().split() for _ in range(num)]
list_a = []
list_b = [0 for _ in range(num)]
for a in range(num):
    input_ob = input().split()
    input_ob[0] = int(input_ob[0])
    input_ob[1] = int(input_ob[1])
    list_a.append(input_ob)
    for b in range(a+1):
        if not list_a[b][0] == input_ob[0]:
            if input_ob[1] > list_a[b][1]:
                list_b[a] += list_a[b][1]
            elif input_ob[1] < list_a[b][1]:
                list_b[b] += input_ob[1]
[print(c) for c in list_b]
############################################################################################
# https://www.acmicpc.net/problem/10800 문제 제목 : 컬러볼 , 언어 : Python, 날짜 : 2020-02-29, 결과 : 실패
"""
    회고:
    백준을 처음 접했을때 시도해보았던 문제다. 아마 그때도 처음에 O(N^2)으로 풀었던거같은데 오늘도 잘못된 방법임을 알지만 그렇게 시도하긴 했다.
    그래서 곰곰히 고민하다 도저히 안되겠어서 검색을 해봤더니 대단하신분들이 많았다. 정렬을 한다는 아이디어는 접근을 했지만 내가 시도했던 코드는
    최적화했다고 생각했던 코드가 결국에는 O(NlogN) + O(N^2)이였다. 물론 아직도 못풀긴했다. 같은 크기의 경우를 어떻게 처리해주냐가 관건인데
    내일 한번 더 시도해봐야겠다.
    
    
"""

import sys

N = int(sys.stdin.readline())
list_command = [list(map(int, sys.stdin.readline().split()))+[_] for _ in range(N)]
list_command = sorted(list_command, key = lambda a : a[1])
now_sum = 0
list_result = [0]*N
list_color = [0]*(N+1)
index_count = 0
former_ball = -1
former_color = -1
save_sum = -1
imsi_queue = []
for ball in list_command:
    if not ball[1] == former_ball:
        list_result[ball[2]] = now_sum - list_color[ball[0]]
        save_sum = now_sum
        list_color[ball[0]]+=ball[1]
        former_color = ball[0]
        while imsi_queue:
            imsi = imsi_queue.pop()
            list_color[imsi[0]]+=imsi[1]
    else:
        if former_color == ball[0]:
            list_result[ball[2]] = save_sum
        else:
            list_result[ball[2]] = save_sum - list_color[ball[0]]

        imsi_queue.append([ball[0],ball[1]])

    former_ball = ball[1]
    now_sum+=ball[1]
    index_count += 1

[print(ball) for ball in list_result]
###############################################################################################
# https://www.acmicpc.net/problem/10800 문제 제목 : 컬러볼 , 언어 : Python, 날짜 : 2020-03-01(!!!), 결과 : 성공
"""
    회고:
    중복 처리 방법 : 우선 정렬된 공들을 가지고 누적합을 구해나갈때 이전과 같은 값인지부터 비교를한다. 만약 같은값이라면,
    현재 index - 1번째에 했던 행동들(누적합 구하기, 컬러별 누적합 구하기)를 취소해 준다. 그리고 중복이 끝나면 처리할 공들을 모아놓은 리스트인
    imsi_stack에 넣어준다. 만약 현재 공이 중복되지않는 공이라면 기존의 imsi_stack에 대한 연산을 해 주고 난뒤 현재 연산을 한다.
    솔직히 내가 한 말이지만 먼 이야기인지 모르겠다. 나중에 다시 작성을 해봐야겠다.
    
    일기: 오늘은 정말 운수좋은 날인것 같아 작성해본다.
    요즘 시국이 시국인지라 뉴스만 나와도 겁이난다. 내가 사는 동네에도 갑자기 확진자가 나오기 시작했다. 하루빨리 이 사태가 잠잠해지고
    대학에 가 그동안 하고 싶었던 공부를 하고싶다. 게다가 오늘은 정말 운이 없는 것 같다. 기존에 시켰던 마스크가 취소당하고 어렵게 또 마스크를 
    구매했는데 알고보니 어린이용이였다. 그리고 홈쇼핑에 전화로만 판매하는 마스크가 있는데 전화연결에 성공했는데 정보를 입력하다가 이만 끊겨버렸다..
    그리고 오늘 그릇을 깨뜨렸다.
    내일은 오늘보단 좋겠지.
"""


import sys

N = int(sys.stdin.readline())
list_balls = [list(map(int, sys.stdin.readline().split()))+[_] for _ in range(N)]
list_balls = sorted(list_balls, key = lambda a : (a[1],a[0]))
list_print = [-1]*(N)

list_color = [0]*(N+1)
now_sum = 0
former_ball = list_balls[0]
imsi_stack = []
count = 0
token = 0
for now_ball in list_balls:
    if former_ball[1] == now_ball[1]:
        if token == 0 and count >= 1:
            now_sum -= list_balls[count-1][1]
            list_color[list_balls[count-1][0]] -= list_balls[count-1][1]
            imsi_stack.append(list_balls[count-1])
        list_print[now_ball[2]] = now_sum - list_color[now_ball[0]]
        imsi_stack.append(now_ball)
        token = 1
    else:
        while imsi_stack:
            imsi_ball = imsi_stack.pop()
            list_color[imsi_ball[0]] += imsi_ball[1]
            now_sum += imsi_ball[1]
        list_print[now_ball[2]] = now_sum - list_color[now_ball[0]]
        list_color[now_ball[0]] += now_ball[1]
        now_sum += now_ball[1]
        token = 0
    former_ball = now_ball
    count+=1
[print(a) for a in list_print]
