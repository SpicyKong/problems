# https://www.acmicpc.net/problem/17143 문제 제목 : 낚시왕 , 언어 : Python, 날짜 : 2020-01-15, 결과 : 성공
# 이 문제는 정말 머리가 괴로웠다.
# 구현이 까다로웠던 것도, 알고리즘 설계하는것도 어려운것이 없었는데 왜 이렇게 어렵게 느껴졌는지 모르겠다.
# 구현하면서 몇가지 트릭(?)아닌 트릭을 썼는데 뭐 당연한것들일수도 있겠지만
# 나로서는 이러한 생각들을 한 후 뿌듯했다.
"""

step -
    0. R,C,M을 입력받고 list_info_sharks를 채워나간다.
    1. 낚시왕이 오른쪽으로 한칸 이동후 잡을 상어의 c좌표를 0으로 수정한후  
       result +=  상어의 사이즈
    2. 0으로 초기화된 R*C 크기의 리스트에서 이동후의 좌표에 각각 상어의 정보를 
       복사해둔다.
    3. 만약 같은 좌표에 이미 상어가 존재하다면, 두 상어의 사이즈를 비교하고 작은
       상어의 c좌표를 0으로 수정한다.
"""

import sys


input_a = sys.stdin.readline
R, C, M = map(int, input_a().split())
list_info_sharks = [[] for _ in range(C+1)]
dx = [0, 0, 0, 1, -1]
dy = [0, -1, 1, 0, 0]
result = 0
for _ in range(M): # list_info_sharks[c]에 상어의 c좌표에 따라 정리해둔다.
    input_info_shark = list(map(int, input_a().split()))
    list_info_sharks[input_info_shark[1]].append(input_info_shark)

for now_c in range(1, C+1):

    ##################################################################

    close_distance = 1000
    close_index = -1
    for catch_index, catch_info in enumerate(list_info_sharks[now_c]):
        if catch_info[0] < close_distance and catch_info[1]:
            close_distance = catch_info[0]
            close_index = catch_index
    if not close_index == -1:
        list_info_sharks[now_c][close_index][1] = 0
        result += list_info_sharks[now_c][close_index][4]
    ##################################################################
    list_check = [[0]*(C+1) for _ in range(R+1)]
    save_info_sharks = [[] for _ in range(C+1)]
    for i in range(1, C+1):
        while list_info_sharks[i]:
            save_info = list_info_sharks[i].pop()
            if save_info[1]:
                save_info[0] += dy[save_info[3]]*save_info[2]
                save_info[1] += dx[save_info[3]]*save_info[2]
                if save_info[0] > R:
                    imsi_quotient  = (save_info[0] - R - 1) //(R - 1)
                    imsi_remainder = (save_info[0] - R - 1) % (R - 1)

                    if imsi_quotient % 2 == 0:
                        save_info[0] = R - 1 - imsi_remainder
                        save_info[3] = 1
                    else:
                        save_info[0] = 2 + imsi_remainder
                        save_info[3] = 2
                elif save_info[0] < 1:
                    imsi_quotient  = (save_info[0]*(-1)) //(R - 1)
                    imsi_remainder = (save_info[0]*(-1)) % (R - 1)
                    if imsi_quotient % 2 == 0:
                        save_info[0] = 2 + imsi_remainder
                        save_info[3] = 2
                    else:
                        save_info[0] = R - 1 -imsi_remainder
                        save_info[3] = 1
                if save_info[1] > C:
                    imsi_quotient  = (save_info[1] - C - 1) //(C - 1)
                    imsi_remainder = (save_info[1] - C - 1) % (C - 1)

                    if imsi_quotient % 2 == 0:
                        save_info[1] = C - 1 - imsi_remainder
                        save_info[3] = 4
                    else:
                        save_info[1] = 2 + imsi_remainder
                        save_info[3] = 3
                elif save_info[1] < 1:
                    imsi_quotient  = (save_info[1]*(-1)) //(C - 1)
                    imsi_remainder = (save_info[1]*(-1)) % (C - 1)
                    if imsi_quotient % 2 == 0:
                        save_info[1] = 2 + imsi_remainder
                        save_info[3] = 3
                    else:
                        save_info[1] = C - 1 -imsi_remainder
                        save_info[3] = 4
                save_info_sharks[save_info[1]].append(save_info)
                if list_check[save_info[0]][save_info[1]]:
                    if list_check[save_info[0]][save_info[1]][4] > save_info[4]:
                        save_info[1] = 0
                    else:
                        list_check[save_info[0]][save_info[1]][1] = 0
                        list_check[save_info[0]][save_info[1]] = save_info
                else:
                    list_check[save_info[0]][save_info[1]] = save_info
    list_info_sharks = list(save_info_sharks)



print(result)

"""


    -12 -13 -14 -15 -16 -17
-11 -10 -9  -8  -7  -6
     0  -1  -2  -3  -4  -5
 1   2   3   4   5   6   7
 13  12  11  10  9   8 
     14  15  16  17  18  19
 25  24  23  22  21  20
     26  27  28  29  30  31

     13  14  15  16  17  18
 12  11  10  9   8   7
     1   2   3   4   5   6

 6   5   4   3   2   1 
     7   8   9   10  11  12
 18  17  16  15  14  13
     19  20  21  22  23  24
(20 - 7 - 1) % 6
"""
"""
list_a = [[3, 4], [1, 2]]
list_b = [[0, 0, 0] ,[0, 0, 0], [0, 0, 0]]
list_c = []
test_a = list_a.pop()
list_b[test_a[0]][test_a[1]] = test_a
list_c.append(test_a)
test_a = list_a.pop()
list_b[1][2][0] =1000
list_b[1][2] = test_a
print(list_c)
print(list_b)"""
