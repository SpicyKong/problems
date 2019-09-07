# https://www.acmicpc.net/problem/14891 문제 제목 : 톱니바퀴 , 언어 : Python, 날짜 : 2019-09-07, 결과 : 성공

import sys

list_topni = [list(map(int, list(sys.stdin.readline())[:-1])) for _ in range(4)]
K = int(sys.stdin.readline())
for _ in range(K):
    list_a = [0,0,0,0]
    a,b = map(int, sys.stdin.readline().split())
    list_a[a-1] = b
    for c in range(4-a): # 오른쪽
        if not list_topni[a+c][6] == list_topni[a+c-1][2]:
            list_a[a+c] = list_a[a+c-1]*-1
        else:
            break
    for d in range(a-1): # 왼쪽
        if not list_topni[a-d-1][6] == list_topni[a-d-2][2]:
            list_a[a-d-2] = list_a[a-d-1]*-1
    for e in range(4):
        if list_a[e]==0:
            pass
        elif list_a[e] == -1:
            save_num = list_topni[e].pop(0)
            list_topni[e].append(save_num)
        elif list_a[e] == 1:
            save_num = list_topni[e].pop(-1)
            list_topni[e].insert(0,save_num)
result = 0
if list_topni[0][0] == 1:
    result+=1
if list_topni[1][0] == 1:
    result+=2
if list_topni[2][0] == 1:
    result+=4
if list_topni[3][0] == 1:
    result+=8
print(result)
