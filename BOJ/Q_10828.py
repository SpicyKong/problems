# https://www.acmicpc.net/problem/10828 문제 제목 : 스택 , 언어 : Python, 날짜 : 2019-08-26, 결과 : 성공

import sys

N = int(sys.stdin.readline())
stack_list = []
for _ in range(N):
    test_a = sys.stdin.readline().split()
    if test_a[0]== 'push':
        stack_list.append(test_a[1])
    elif test_a[0] == 'pop':
        #print('popasdd')
        if len(stack_list) > 0:
            a = stack_list.pop()
            print(a)
            #del stack_list[-1]
        else:
            print(-1)
    elif test_a[0] == 'size':
        print(len(stack_list))
    elif test_a[0] == 'empty':
        if len(stack_list) == 0:
            print(1)
        else:
            print(0)
    elif test_a[0] =='top':
        try:
            print(stack_list[-1])
        except:
            print(-1)
    #print(stack_list)
