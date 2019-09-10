# https://www.acmicpc.net/problem/2606 문제 제목 : 바이러스 , 언어 : Python, 날짜 : 2019-09-10, 결과 : 실패(메모리 초과)

import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
list_network = [list(map(int, sys.stdin.readline().split()))] # 처음받은 입력은 그냥 넣어줍니다.
for _ in range(M-1):
    input_a, input_b = map(int, sys.stdin.readline().split())
    for n,a in enumerate(list_network):
        is_there_a = input_a in a\
        is_there_b = input_b in a
        if is_there_a and not is_there_b: # 현재 네트워크에 첫번째 입력은 있고 두번째 입력은 없다면 
            list_network[n].append(input_b)# 두번째 입력을 현재 네트워크에 추가해 줍니다
        elif not is_there_a and is_there_b:
            list_network[n].append(input_a)
        elif not is_there_a and not is_there_b:# 둘다 없다면 새로운 네트워크를 구성합니다.
            list_network.append([input_a,input_b])
for a in list_network: # 1번이 있는 네트워크를 찾고 감염된 PC수를 구합니다.
    if 1 in a:
        print(len(a)-1)
        break
