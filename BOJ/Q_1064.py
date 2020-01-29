# https://www.acmicpc.net/problem/1064 문제 제목 : 평행사변형 , 언어 : Python, 날짜 : 2020-01-29, 결과 : 성공

import sys

def twopoint(point1, point2): # this function return [length, gradient]
    x = point1[0] - point2[0]
    y = point1[1] - point2[1]
    length = (x**2 + y**2)**0.5
    if x==0:
        gradient='INF'
    else:
        gradient = y/x
    return [length, gradient]

A_x, A_y, B_x, B_y, C_x, C_y = map(int, sys.stdin.readline().split())
point_a = [A_x, A_y]
point_b = [B_x, B_y]
point_c = [C_x, C_y]
#gradient
line_ab = twopoint(point_a,point_b)#[0,0] # length, gradient
line_ac = twopoint(point_a,point_c)#[0,0]
line_bc = twopoint(point_b,point_c)#[0,0]
list_info = [length[0] for length in [line_ab, line_ac, line_bc]]
if line_ab[1] == line_ac[1] == line_bc[1]:
    print(-1)
else:
    """
    (lena + lenb)*2 - (lenb + lenc)*2
    2lena -2lenc
    """
    print((max(list_info) - min(list_info))*2)
