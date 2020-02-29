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
