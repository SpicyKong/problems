# https://www.acmicpc.net/problem/14499 문제 제목 : 주사위 굴리기 , 언어 : Python, 날짜 : 2019-09-06 > 2019-09-07 , 결과 : 성공

# 이 문제는 문제를 진짜 잘 읽어 봐야한다.. x랑 y.. 낚여씀
# 문제 읽는 연습 하기!

import sys

N, M, x, y, K = map(int, sys.stdin.readline().split())
list_map = [0]*M
list_map = [list_map]*N
dice = [0, 0, 0, 0, 0, 0]
#   [2, 1, 5, 6, 4, 3]
def func_act(num):
    global dice
    save_num = 0
    if num == 1:# [2, 4, 5, 3, 6, 1]
        save_num = dice[1]
        dice[1] = dice[4]
        dice[4] = dice[3]
        dice[3] = dice[5]
        dice[5] = save_num
    elif num == 2: #[2, 3, 5, 4, 1, 6]
        save_num = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[3]
        dice[3] = dice[4]
        dice[4] = save_num
    elif num == 3: # [1, 5, 6, 2, 4, 3]
        save_num = dice[1]
        dice[1] = dice[2]
        dice[2] = dice[3]
        dice[3] = dice[0]
        dice[0] = save_num
    elif num == 4:# [6, 2, 1, 5, 4, 3]
        save_num = dice[1]
        dice[1] = dice[0]
        dice[0] = dice[3]
        dice[3] = dice[2]
        dice[2] = save_num
    #return dice
for a in range(N):
    list_a = list(map(int, sys.stdin.readline().split()))
    list_map[a]=list_a[:]

for act in list(map(int, sys.stdin.readline().split())):
    
    q_act = 0
    if act==1:
        if y < M-1:
            y+=1
            q_act = 1
    elif act==2:
        if y > 0:
            y-=1
            q_act = 1
    elif act==3:
        if x > 0:
            x-=1
            q_act = 1
    elif act==4:
        if x < N-1:
            x+=1
            q_act = 1
    if q_act ==1:
        
        func_act(act)
        if list_map[x][y] == 0:
            list_map[x][y] = dice[3]
        else:
            dice[3] = list_map[x][y]
            list_map[x][y] = 0
        print(dice[1])
