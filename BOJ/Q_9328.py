# https://www.acmicpc.net/problem/9328 문제 제목 : 열쇠 , 언어 : Python, 날짜 : 2020-03-17, 결과 : 성공
"""
    회고:
    솔직히 말하자면 다른분의 풀이를 약간 보고 풀었다. 처음 내가 생각했던 방식은 열쇠를 찾았을때
    (0,0)에서부터 다시 BFS를 돌려주는것이다. 하지만 아무리 생각해도 이렇게 무식하게 풀 문제는 아닌것 같아서
    고민을 하다 다른분의 코드를 참고했다. 놀라웠다. 기존에 탐색을하며 키가 없던 장소는 저장해두었다가
    키를 발견하면 BFS큐에 저장된 좌표를 push해주면 되는 간단한 아이디어가 핵심이였다. 대단한것같다.
    그래도 이제 이런류의 문제를 보면 테두리를 추가해주는 아이디어는 보이는것 같아 신기하다.
"""

import sys
from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]
T = int(sys.stdin.readline())
for _ in range(T):
    h, w = map(int, sys.stdin.readline().split())
    dict_keys = {chr(i+65):0 for i in range(26)}
    dict_xy = {chr(i+65):[] for i in range(26)}
    list_map = [['.']*(w+2)]
    for _ in range(h):
        list_map.append(['.']+list(sys.stdin.readline().strip())+['.'])
    list_map.append(['.']*(w+2))
    list_visit = [[0]*(w+2) for _ in range(h+2)]
    #[print(a) for a in list_map]
    #[print(a) for a in list_visit]
    for key in sys.stdin.readline().strip():
        dict_keys[key.upper()] = 1
    list_queue = deque()
    list_queue.append([0,0])
    result = 0
    while list_queue:
        now_x, now_y = list_queue.popleft()
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if 0 <= nx < w+2 and 0 <= ny < h+2:
                if list_map[ny][nx] == '.' and not list_visit[ny][nx]:
                    list_queue.append([nx,ny])
                    list_visit[ny][nx]=1
                elif list_map[ny][nx] == '$' and not list_visit[ny][nx]:
                    list_queue.append([nx,ny])
                    list_visit[ny][nx]=1
                    result+=1
                elif 'a' <= list_map[ny][nx] <= 'z' and not list_visit[ny][nx]:
                    list_queue.append([nx,ny])
                    list_visit[ny][nx]=1
                    big_letter = list_map[ny][nx].upper()
                    dict_keys[big_letter] = 1
                    if dict_xy[big_letter]:
                        while dict_xy[big_letter]:
                            list_queue.append(dict_xy[big_letter].pop())
                elif 'A' <= list_map[ny][nx] <= 'Z' and not list_visit[ny][nx]:
                    if dict_keys[list_map[ny][nx]]:
                        list_queue.append([nx,ny])
                        list_visit[ny][nx]=1
                    else:
                        dict_xy[list_map[ny][nx]].append([now_x, now_y])
    print(result)
