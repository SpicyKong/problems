# https://www.acmicpc.net/problem/1041 문제 제목 : 주사위 , 언어 : Python, 날짜 : 2019-12-27, 결과 : 실패
# https://www.acmicpc.net/problem/1041 문제 제목 : 주사위 , 언어 : Python, 날짜 : 2020-01-22, 결과 : 성공
# one_side함수가 max값을 반환하는것을 못봐서 삽질햇다..ㅠ
# 바로아래에는 삼질하면서 줄인 코드고 그밑에는 원래 코드다.
import sys
"""
1면:
    (N-2)**2
    (N-2)*(N-1)*4
2면:
    (N-2)*4
    (N-1)*4
3면:
    4
"""
def one_side(dice):
    return min(dice)
def two_side(dice):
    min_num = 101
    for i,num1 in enumerate(dice):
        for j,num2 in enumerate(dice):
            if not i + j == 5 and not i == j:
                if num1 + num2 < min_num:
                    min_num = num1 + num2
    return min_num
def three_side(dice):
    return min(dice[0], dice[5]) + min(dice[1], dice[4]) + min(dice[2], dice[3])
N = int(sys.stdin.readline())
list_dice = list(map(int, sys.stdin.readline().split()))

if N == 1:
    print(sum(list_dice) - max(list_dice))
else:
    result = 0
    result += one_side(list_dice) * ((N-2)**2 + (N-2)*(N-1)*4)
    result += two_side(list_dice) * ((N-2)*4 + (N-1)*4)
    result += three_side(list_dice) * 4
    print(result)

    
    
    
# 이 코드도 정답코드인데 맨처음에 반환값이 max(dice)인것을 못보고 삽질했다..
import sys

def one_side(dice):
    return min(dice)
def two_side(dice):
    min_num = min([dice[1] + dice[2], dice[2] + dice[4], dice[3] + dice[4], dice[3] + dice[1]])
    for i in range(1,5):
        min_save = min(dice[0] + dice[i], dice[5] + dice[i])
        if min_save < min_num:
            min_num = min_save
    return min_num

def three_side(dice):
    # (0,5) (1,4) (2,3)
    min_side = min(dice)
    min_side_index = 0
    for i, num in enumerate(dice):
        if num == min_side:
            min_side_index = i
    opposite_side_index = abs(5-min_side_index)
    #list_four_side = [num for i, num in enumerate(dice) if not i==min_side_index or not i==opposite_side_index]
    min_num = 101
    for i,num1 in enumerate(dice):
        if not i==min_side_index and not i==opposite_side_index:
            for j,num2 in enumerate(dice):
                if not i == j and not j==min_side_index and not j==opposite_side_index and not i + j==5:
                    if min_num > (dice[i] + dice[j]):
                        min_num = dice[i] + dice[j]
    return min_num + dice[min_side_index]


N = int(sys.stdin.readline())
list_dice = list(map(int, sys.stdin.readline().split()))

if N == 1:
    print(sum(list_dice) - max(list_dice))
else:
    result = 0
    result += one_side(list_dice) * ((N-2)**2 + (N-2)*(N-1)*4)
    result += two_side(list_dice) * ((N-2)*4 + (N-1)*4)
    result += three_side(list_dice) * 4
    print(result)

# 시간초과 코드
# 시간초과가 어디서 나는건지,...

import sys
N = int(sys.stdin.readline())
list_dice = list(map(int, sys.stdin.readline().split()))
one_corner = min(list_dice)
double_corner = 102

for i in range(3):
    list_imsi = list_dice[:i] + list_dice[i+1:5-i]
    try:
        list_imsi += list_dice[5-i+1:]
    except:
        pass
    #print(i, ":", list_imsi)#list_dice[:i], list_dice[i+1:5-i], i+1,5-i)
    lesser = min(list_imsi)
    if double_corner > lesser + list_dice[i]:
        double_corner = lesser + list_dice[i]
    
    if double_corner > lesser + list_dice[5-i]:
        double_corner = lesser + list_dice[5-i]


third_corner = min([list_dice[0] + list_dice[1] + list_dice[2], list_dice[0] + list_dice[1] + list_dice[3], list_dice[0] + list_dice[3] + list_dice[4], list_dice[0] + list_dice[2] + list_dice[4], list_dice[5] + list_dice[1] + list_dice[2], list_dice[5] + list_dice[1] + list_dice[3], list_dice[5] + list_dice[3] + list_dice[4], list_dice[5] + list_dice[2] + list_dice[4]])
#print(one_corner, double_corner, third_corner)
if N == 1:
    print(sum(list_dice) - sorted(list_dice)[-1])
elif N == 2:
    print(third_corner*4 + double_corner*4)
else:
    print(third_corner*4 + double_corner*4*(N-1) + double_corner*4*(N-2) + one_corner*(N-2)*(N-1)*4 +  one_corner**(N-2))
