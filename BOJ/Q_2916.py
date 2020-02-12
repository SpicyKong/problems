# https://www.acmicpc.net/problem/2916 문제 제목 : 자와 각도기 , 언어 : Python, 날짜 : 2020-02-12, 결과 : 성공
# 겁먹고 건들지도 못하고 있었는데 막상 푸니깐 맞았다ㅋㅋ

import sys

N, K = map(int, sys.stdin.readline().split())
list_angles_know = list(map(int, sys.stdin.readline().split()))
list_angles_goal = list(map(int, sys.stdin.readline().split()))
angles = [0]*360

def func_a(angle):
    global list_angles_know, angles
    if angles[angle]:
        return
    else:
        list_angles_know.append(angle)
        angles[angle] = 1
    for angle_now in list_angles_know:
        func_a((angle_now+angle)%360)
        func_a(abs(angle_now-angle)%360)
func_a(0)
for angle in list_angles_goal:
    if angles[angle]:
        print('YES')
    else:
        print('NO')
