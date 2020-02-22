# https://www.acmicpc.net/problem/1360 문제 제목 : 되돌리기 , 언어 : Python, 날짜 : 2020-02-22, 결과 : 성공
"""
    회고:
    이 문제는 쉬워 보여서 건드려 보았는데 플레였다. 근데 실버문제같은 난이도이다. 그냥 썡으로 구현하면
    되는 문제라 쉬웠는데 첫번째 시도에서는 런타임 에러가 떠서 생각하다가 두번째 반복문(처리하는 반복문)
    안에있는 while문에서 i-j의 값을 보장해주니깐 맞았다. 이문제의 <<<<순서로 생각하는것이다.
    요즘 코로나 바이러스가 기승인데 학교나 제대로 갈수있을련지 의문이다..ㅠㅠ
"""
import sys
N = int(sys.stdin.readline())
command_list = []
command_check = []
command_time = []
for _ in range(N): # 입력받는 반복문
    co, s, t = sys.stdin.readline().split()
    command_list.append(s)
    command_check.append(0)
    command_time.append(int(t))
for i in range(N-1,-1,-1): # 처리하는 반복문
    if not 'a' <= command_list[i] <= 'z' and not command_check[i]:
        j = 1
        #print(command_time[i-j] ,command_time[i], command_list[i])
        while i-j >= 0 and command_time[i-j] >= command_time[i] - int(command_list[i]):
            command_check[i-j] = 1
            j+=1

for i in range(N):# 출력하는 반복문
    if 'a' <= command_list[i] <= 'z' and not command_check[i]:
        print(command_list[i],end='')
