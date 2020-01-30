# https://www.acmicpc.net/problem/5373 문제 제목 : 큐빙 , 언어 : Python, 날짜 : 2020-01-30, 결과 : 성공

import sys

#asdjkljdal = [['1','2','3'],['4','5','6'],['7','8','9']]
# 큐브 전개도
#   1 
# 5 2 6
#   3 
#   4 

list_cube_1 = ['w','w','w','w','w','w','w','w','w']
list_cube_2 = ['r','r','r','r','r','r','r','r','r']
list_cube_3 = ['y','y','y','y','y','y','y','y','y']
list_cube_4 = ['o','o','o','o','o','o','o','o','o']
list_cube_5 = ['g','g','g','g','g','g','g','g','g']
list_cube_6 = ['b','b','b','b','b','b','b','b','b']
def U():
    global list_cube_1, list_cube_2, list_cube_3, list_cube_4, list_cube_5, list_cube_6
    save_corner = list_cube_1[8]
    list_cube_1[8] = list_cube_1[2]
    list_cube_1[2] = list_cube_1[0]
    list_cube_1[0] = list_cube_1[6]
    list_cube_1[6] = save_corner
    save_corner = list_cube_1[1]
    list_cube_1[1] = list_cube_1[3]
    list_cube_1[3] = list_cube_1[7]
    list_cube_1[7] = list_cube_1[5]
    list_cube_1[5] = save_corner
    
    save_0 = list_cube_2[0]
    save_1 = list_cube_2[1]
    save_2 = list_cube_2[2]
    
    list_cube_2[0] = list_cube_6[0]
    list_cube_2[1] = list_cube_6[1]
    list_cube_2[2] = list_cube_6[2]
    
    list_cube_6[0] = list_cube_4[0]
    list_cube_6[1] = list_cube_4[1]
    list_cube_6[2] = list_cube_4[2]
    
    list_cube_4[0] = list_cube_5[0]
    list_cube_4[1] = list_cube_5[1]
    list_cube_4[2] = list_cube_5[2]
    
    list_cube_5[0] = save_0
    list_cube_5[1] = save_1
    list_cube_5[2] = save_2

def D():
    global list_cube_1, list_cube_2, list_cube_3, list_cube_4, list_cube_5, list_cube_6
    save_corner = list_cube_3[8]
    list_cube_3[8] = list_cube_3[2]
    list_cube_3[2] = list_cube_3[0]
    list_cube_3[0] = list_cube_3[6]
    list_cube_3[6] = save_corner
    save_corner = list_cube_3[1]
    list_cube_3[1] = list_cube_3[3]
    list_cube_3[3] = list_cube_3[7]
    list_cube_3[7] = list_cube_3[5]
    list_cube_3[5] = save_corner
    
    save_6 = list_cube_2[6]
    save_7 = list_cube_2[7]
    save_8 = list_cube_2[8]
    
    list_cube_2[6] = list_cube_5[6]
    list_cube_2[7] = list_cube_5[7]
    list_cube_2[8] = list_cube_5[8]

    list_cube_5[6] = list_cube_4[6]
    list_cube_5[7] = list_cube_4[7]
    list_cube_5[8] = list_cube_4[8]

    list_cube_4[6] = list_cube_6[6]
    list_cube_4[7] = list_cube_6[7]
    list_cube_4[8] = list_cube_6[8]

    list_cube_6[6] = save_6
    list_cube_6[7] = save_7
    list_cube_6[8] = save_8

def F():
    global list_cube_1, list_cube_2, list_cube_3, list_cube_4, list_cube_5, list_cube_6
    
    save_corner = list_cube_2[8]
    list_cube_2[8] = list_cube_2[2]
    list_cube_2[2] = list_cube_2[0]
    list_cube_2[0] = list_cube_2[6]
    list_cube_2[6] = save_corner
    save_corner = list_cube_2[1]
    list_cube_2[1] = list_cube_2[3]
    list_cube_2[3] = list_cube_2[7]
    list_cube_2[7] = list_cube_2[5]
    list_cube_2[5] = save_corner

    save1 = list_cube_1[6]
    save2 = list_cube_1[7]
    save3 = list_cube_1[8]
    
    list_cube_1[6] = list_cube_5[8]
    list_cube_1[7] = list_cube_5[5]
    list_cube_1[8] = list_cube_5[2]

    list_cube_5[8] = list_cube_3[2]
    list_cube_5[5] = list_cube_3[1]
    list_cube_5[2] = list_cube_3[0]

    list_cube_3[2] = list_cube_6[0]
    list_cube_3[1] = list_cube_6[3]
    list_cube_3[0] = list_cube_6[6]
    
    list_cube_6[0] = save1
    list_cube_6[3] = save2
    list_cube_6[6] = save3

def B():
    global list_cube_1, list_cube_2, list_cube_3, list_cube_4, list_cube_5, list_cube_6
    
    save_corner = list_cube_4[8]
    list_cube_4[8] = list_cube_4[2]
    list_cube_4[2] = list_cube_4[0]
    list_cube_4[0] = list_cube_4[6]
    list_cube_4[6] = save_corner
    save_corner = list_cube_4[1]
    list_cube_4[1] = list_cube_4[3]
    list_cube_4[3] = list_cube_4[7]
    list_cube_4[7] = list_cube_4[5]
    list_cube_4[5] = save_corner

    save1 = list_cube_1[0]
    save2 = list_cube_1[1]
    save3 = list_cube_1[2]

    list_cube_1[0] = list_cube_6[2]
    list_cube_1[1] = list_cube_6[5]
    list_cube_1[2] = list_cube_6[8]

    list_cube_6[2] = list_cube_3[8]
    list_cube_6[5] = list_cube_3[7]
    list_cube_6[8] = list_cube_3[6]

    list_cube_3[8] = list_cube_5[6]
    list_cube_3[7] = list_cube_5[3]
    list_cube_3[6] = list_cube_5[0]

    list_cube_5[6] = save1
    list_cube_5[3] = save2
    list_cube_5[0] = save3

def R():
    global list_cube_1, list_cube_2, list_cube_3, list_cube_4, list_cube_5, list_cube_6
    
    save_corner = list_cube_6[8]
    list_cube_6[8] = list_cube_6[2]
    list_cube_6[2] = list_cube_6[0]
    list_cube_6[0] = list_cube_6[6]
    list_cube_6[6] = save_corner
    save_corner = list_cube_6[1]
    list_cube_6[1] = list_cube_6[3]
    list_cube_6[3] = list_cube_6[7]
    list_cube_6[7] = list_cube_6[5]
    list_cube_6[5] = save_corner

    save1 = list_cube_1[2]
    save2 = list_cube_1[5]
    save3 = list_cube_1[8]
    
    list_cube_1[2] = list_cube_2[2]
    list_cube_1[5] = list_cube_2[5]
    list_cube_1[8] = list_cube_2[8]
    
    list_cube_2[2] = list_cube_3[2]
    list_cube_2[5] = list_cube_3[5]
    list_cube_2[8] = list_cube_3[8]
    
    list_cube_3[2] = list_cube_4[6]
    list_cube_3[5] = list_cube_4[3]
    list_cube_3[8] = list_cube_4[0]
    
    list_cube_4[6] = save1
    list_cube_4[3] = save2
    list_cube_4[0] = save3


def L():
    global list_cube_1, list_cube_2, list_cube_3, list_cube_4, list_cube_5, list_cube_6
    
    save_corner = list_cube_5[8]
    list_cube_5[8] = list_cube_5[2]
    list_cube_5[2] = list_cube_5[0]
    list_cube_5[0] = list_cube_5[6]
    list_cube_5[6] = save_corner
    save_corner = list_cube_5[1]
    list_cube_5[1] = list_cube_5[3]
    list_cube_5[3] = list_cube_5[7]
    list_cube_5[7] = list_cube_5[5]
    list_cube_5[5] = save_corner

    save1 = list_cube_1[0]
    save2 = list_cube_1[3]
    save3 = list_cube_1[6]

    list_cube_1[0] = list_cube_4[8]
    list_cube_1[3] = list_cube_4[5]
    list_cube_1[6] = list_cube_4[2]

    list_cube_4[8] = list_cube_3[0]
    list_cube_4[5] = list_cube_3[3]
    list_cube_4[2] = list_cube_3[6]

    list_cube_3[0] = list_cube_2[0]
    list_cube_3[3] = list_cube_2[3]
    list_cube_3[6] = list_cube_2[6]

    list_cube_2[0] = save1
    list_cube_2[3] = save2
    list_cube_2[6] = save3

func_dict = {'U':U, 'F':F, 'D':D, 'B':B, 'R':R, 'L':L}
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    for action in sys.stdin.readline().strip().split():
        func_dict[action[0]]()
        if action[1] == '-':
            func_dict[action[0]]()
            func_dict[action[0]]()
    for i,n in enumerate(list_cube_1):
        print(n, end='')
        if (i+1)%3==0:
            print()
    list_cube_1 = ['w','w','w','w','w','w','w','w','w']
    list_cube_2 = ['r','r','r','r','r','r','r','r','r']
    list_cube_3 = ['y','y','y','y','y','y','y','y','y']
    list_cube_4 = ['o','o','o','o','o','o','o','o','o']
    list_cube_5 = ['g','g','g','g','g','g','g','g','g']
    list_cube_6 = ['b','b','b','b','b','b','b','b','b']
