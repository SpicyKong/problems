# https://www.acmicpc.net/problem/1041 문제 제목 : 주사위 , 언어 : Python, 날짜 : 2019-12-27, 결과 : 실패
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
