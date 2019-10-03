# https://www.acmicpc.net/problem/1929 문제 제목 : 소수 구하기 , 언어 : Python, 날짜 : 2019-10-03, 결과 : 성공

import sys

a, b = map(int, sys.stdin.readline().split())
list_a = [1]+[1]+[0]*(b-1)
asdf = True
index = 2
save_index = 2
while asdf:
    if index <= b:
        if list_a[index] == 0:
            save_index = index*2
            sdfg = True
            while sdfg:
                if save_index <= b:
                    if not list_a[save_index]:
                        list_a[save_index]=1
                else:
                    break
                save_index+=index
    else:
        asdf = False
    index+=1
[print(i) for i in range(1,b+1) if not list_a[i] and a <= i <= b]
