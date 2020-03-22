# https://www.acmicpc.net/problem/1987 문제 제목 : 알파벳 , 언어 : Python, 날짜 : 2019-10-23, 결과 : 실패
# BFS만 풀다보니 DFS문제인데 자꾸 BFS로 짜진다..
# 그냥 BFS로 풀지그랬어ㅠㅠ - 2020.03.22


import sys
R, C = map(int, sys.stdin.readline().split())
list_visit = [[0]*C for _ in range(R)]
list_map = [list(sys.stdin.readline()) for _ in range(R)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
list_stack = [[0, 0]]
list_alphabet = [list_map[0][0]]
check_is_there = 0
max_num = 0
now_num = 0
while list_stack:
    x, y = list_stack[-1]
    list_alphabet.append(list_map[y][x])
    count_i = 0
    asdf = 0
    while not count_i == 3 and not asdf:
        ax = x + dx[count_i]
        ay = y + dy[count_i]
        if 0 <= ax < C and 0 <= ay < R:
            if list_visit[ay][ax] == 0 and not list_map[ay][ax] in list_alphabet:
                list_visit[ay][ax] = 1
                list_stack.append([ax, ay])
                asdf = True
                check_is_there = 1
                now_num +=1
        count_i += 1
    if max_num < now_num:
        max_num = now_num
    if not check_is_there:
        tx, ty = list_stack.pop()
        list_visit[ty][tx] = 0
        list_alphabet.pop()
        now_num -= 1
    else:
        check_is_there = 0
    print(list_stack)
    print("=====================")
print(max_num)
    


"""
while list_stack:
    x, y = list_stack.pop()
    list_alphabet.append(list_map[y][x])
    for i in range(2):
        ax = x + dx[i]
        ay = y + dy[i]
        if 0 <= ax < C and 0 <= ay < R:
            if list_visit[ay][ax] == 0 and not list_map[ay][ax] in list_alphabet:
                list_visit[ay][ax] = 1
                list_stack.append([ax, ay])
    [print(a) for a in list_visit]
    print("=====================")
"""


#######################################################################################################
# https://www.acmicpc.net/problem/1987 문제 제목 : 알파벳 , 언어 : Python, 날짜 : 2020-03-22, 결과 : 성공
"""
    회고:
    주석을 보면 알다시피 이 문제는 많은 전투의 흔적이 남아있다.
    우선 내가 생각하는 문제점은 아마도 파이썬으로 해결하고자 했던것이다.
    분명 같은로직의 코드임에도 다른분들은 맞지만 파이썬코드는 시간초과가 뜬다. 이는 흔한일이긴 하다.
    그냥 탐색을 할때마다 밟고온 알파벳을 처리해주는 간단한 문제인줄알았는데 계속 시간초과가 떠서 찾아보다가
    파이썬의 경우에는 BFS를 돌리라는 말을 보고 BFS로 코드를 짜봤더니 그래도 시간초과가 떴다.
    그래서 한번 더 서칭을 해 보니 set을 사용하라는 조언을 얻었다. 그랬더니 통과했다.

    통과를 하고 생각해보니 이 문제는 경로를 알파벳 26가지를 통해 앞으로의 경로를 생각해낼수있으니
    set을 사용할수있는것이였다. 그러니깐 전에 어디서 왔는지의 정보는 필요없고 (어차피 visited를 체크해주는 배열도 없다.)
    내가 어떤 알파벳을 밟아왔는지에 대한 정보만 있으면 되니 set을 사용할수있는것이다.
    역시 사람들은 대단하다.
    아 원래라면 기존에 작성한 코드를 주석처리 해놓은 부분은 지우고 커밋하는데 이 문제는 그냥 올려야겠다.

"""
import sys
#from collections import deque
N, M = map(int, sys.stdin.readline().split())
list_map = [list(sys.stdin.readline().strip()) for _ in range(N)]
dict_alpha = {chr(i+65):i for i in range(26)}
#visit = 1 << dict_alpha[list_map[0][0]]
#visit1 = [0]*26
#visit1[dict_alpha[list_map[0][0]]] = 1
dx = [1,-1,0,0]
dy = [0,0,1,-1]
result = 0
#list_queue = deque()
#list_queue.append([0,0,1 << dict_alpha[list_map[0][0]],0])
list_queue = set([(0,0,1 << dict_alpha[list_map[0][0]],0)])
while list_queue:
    now_x, now_y, visit, count = list_queue.pop()
    if count > result:
        result = count
    for i in range(4):
        nx = now_x + dx[i]
        ny = now_y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if not visit >> dict_alpha[list_map[ny][nx]] & 1:
                new_viist = visit | 1 << dict_alpha[list_map[ny][nx]]
                list_queue.add((nx, ny, new_viist, count+1))
                #visit |= 1 << dict_alpha[list_map[ny][nx]]
                #dfs(nx,ny,count+1)
                #visit &= ~(1 << dict_alpha[list_map[ny][nx]])
print(result+1)
"""
import sys
def dfs(now_x, now_y, count):
    global result, visit1
    if count > result:
        result = count
    for i in range(4):
        nx = now_x + dx[i]
        ny = now_y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if not visit1[dict_alpha[list_map[ny][nx]]]:
                visit1[dict_alpha[list_map[ny][nx]]] = 1
                dfs(nx,ny,count+1)
                visit1[dict_alpha[list_map[ny][nx]]] = 0
            if not visit >> dict_alpha[list_map[ny][nx]] & 1:
                visit |= 1 << dict_alpha[list_map[ny][nx]]
                dfs(nx,ny,count+1)
                visit &= ~(1 << dict_alpha[list_map[ny][nx]])
    
N, M = map(int, sys.stdin.readline().split())
list_map = [list(sys.stdin.readline().strip()) for _ in range(N)]
dict_alpha = {chr(i+65):i for i in range(26)}
visit = 1 << dict_alpha[list_map[0][0]]
visit1 = [0]*26
visit1[dict_alpha[list_map[0][0]]] = 1
dx = [1,-1,0,0]
dy = [0,0,1,-1]
result = 0
dfs(0,0,1)
print(result)
"""
"""
2 2
AB
CA

3 4
ABBC
ECED
FGDH

2 2
AB
CA

3 4
ABBC
ECED
FGDH

20 20
ABCDEFGHIJKLMNOPQRST
BCDEFGHIJKLMNOPQRSTU
CDEFGHIJKLMNOPQRSTUV
DEFGHIJKLMNOPQRSTUVW
EFGHIJKLMNOPQRSTUVWX
FGHIJKLMNOPQRSTUVWXY
GHIJKLMNOPQRSTUVWXYA
HIJKLMNOPQRSTUVWXYAA
IJKLMNOPQRSTUVWXYAAA
JKLMNOPQRSTUVWXYAAAA
KLMNOPQRSTUVWXYAAAAA
LMNOPQRSTUVWXYAAAAAA
MNOPQRSTUVWXYAAAAAAA
NOPQRSTUVWXYAAAAAAAA
OPQRSTUVWXYAAAAAAAAA
PQRSTUVWXYAAAAAAAAAA
QRSTUVWXYAAAAAAAAAAA
RSTUVWXYAAAAAAAAAAAA
STUVWXYAAAAAAAAAAAAA
TUVWXYZAAAAAAAAAAAAA
"""
