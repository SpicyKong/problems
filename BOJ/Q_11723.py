# https://www.acmicpc.net/problem/11723 문제 제목 : 집합 , 언어 : Python, 날짜 : 2019-08-08, 결과 : 성공

import sys
num = int(sys.stdin.readline())
list_s = []
for a in range(num):
    input_data = sys.stdin.readline().split()
    if len(input_data)>1:
        command = input_data[0]
        num = int(input_data[1])
    else:
        command = input_data[0]
    if command=='add' and not num in list_s:
        list_s.append(num)
    elif command == 'remove' and num in list_s:
        list_s.remove(num)
    elif command == 'check':
        if num in list_s:
            print(1)
        else:
            print(0)
    elif command == 'toggle':
        if num in list_s:
            list_s.remove(num)
        else:
            list_s.append(num)
    elif command == 'all':
        list_s = list(range(1,21))
    else:
        list_s = []
