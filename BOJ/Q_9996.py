# https://www.acmicpc.net/problem/9996 문제 제목 : 한국이 그리울 땐 서버에 접속하지 , 언어 : Python, 날짜 : 2020-02-09, 결과 : 성공

import sys

N = int(sys.stdin.readline())

string_pattern = sys.stdin.readline().strip()

list_pattern1 = []
list_pattern2 = []
len_pattern1 = 0
len_pattern2 = 0
save = 0

for word in string_pattern:
    if save == 0:
        list_pattern1.append(word)
        len_pattern1+=1
    else:
        list_pattern2.append(word)
        len_pattern2+=1
    if word == '*':
        len_pattern1-=1
        list_pattern1.pop()
        save = 1

for i in range(N):
    end = 0
    string = list(sys.stdin.readline().strip())
    if len(string) < len_pattern1 + len_pattern2:
        end = 1
    else:
        for i1 in range(len_pattern1):
            if not string[i1] == list_pattern1[i1]:
                end = 1

        for i2 in range(len_pattern2):
            if not string[-1 - i2] == list_pattern2[-1 - i2]:
                end = 1
    if not end:
        print('DA')
    else:
        print('NE')
