# https://www.acmicpc.net/problem/1331 문제 제목 : 나이트 투어 , 언어 : Python, 날짜 : 2020-01-07, 결과 : 성공

import sys
def Q_1331():
    input_list = [list(sys.stdin.readline()[:-1]) for _ in range(36)]
    input_list = [[ord(input_list[i][0]) - 64,int(input_list[i][1])] for i in range(36)]
    chess_map = [[0]*7 for _ in range(7)]
    dx = [2,2,1,-1,-2,-2,-1,1]
    dy = [1,-1,-2,-2,-1,1,2,2]
    #start_x, start_y = input_list[0]

    for i in range(36):
        x,y = input_list[i]
        chess_map[y][x] = 1
        if i == 35:
            next_x, next_y = input_list[0]
        else:
            next_x, next_y = input_list[i+1]
        v_pass = 0
        for j in range(8):
            if 1 <= x + dx[j] <= 6 and 1 <= y + dy[j] <= 6:
                if i == 35:
                    if next_x == x + dx[j] and next_y == y + dy[j]:
                        v_pass = 1
                else:
                    if next_x == x + dx[j] and next_y == y + dy[j] and not chess_map[next_y][next_x]:
                        v_pass = 1
        if not v_pass:
            print("Invalid")
            return
    print("Valid")
    return
Q_1331()
