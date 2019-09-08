# https://www.acmicpc.net/problem/1244 문제 제목 : 스위치 켜고 끄기 , 언어 : Python, 날짜 : 2019-08-30, 결과 : 실패
# https://www.acmicpc.net/problem/1244 문제 제목 : 스위치 켜고 끄기 , 언어 : Python, 날짜 : 2019-09-08, 결과 : 성공

import sys

N = int(sys.stdin.readline())
list_switch = sys.stdin.readline().split()
N_a = int(sys.stdin.readline())

for _ in range(N_a):
    p, n_s = map(int, sys.stdin.readline().split())
    if p == 1:
        for a in range(n_s,N+1,n_s):
            if list_switch[a-1] == '1':
                list_switch[a-1] = '0'
            else:
                list_switch[a-1] = '1'
    else:
        test = True
        count_a = 1
        if list_switch[n_s-1] == '1':
            list_switch[n_s-1] = '0'
        else:
            list_switch[n_s-1] = '1'
        while test:
            if 0<= n_s-1+count_a < N and 0<= n_s-1-count_a < N:
                if list_switch[n_s-1+count_a] == list_switch[n_s-1-count_a]:
                    if list_switch[n_s-1+count_a] == '1':
                        list_switch[n_s-1+count_a]='0'
                        list_switch[n_s-1-count_a]='0'
                    else:
                        list_switch[n_s-1+count_a]='1'
                        list_switch[n_s-1-count_a]='1'
                    count_a+=1
                else:
                    test=False
            else:
                test=False
    #print(list_switch)
for b in range(1,N+1):
    print(list_switch[b-1],end=' ')
    if b%20==0:
        print()
