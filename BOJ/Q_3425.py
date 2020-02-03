# https://www.acmicpc.net/problem/3425 문제 제목 : 고스택 , 언어 : Python, 날짜 : 2020-02-03, 결과 : 성공
# 12회 시도해서 성공했다.
# 하루종일 삽질했는데 알고보니 공백을 출력 맨마지막 공백을 출력 안한거였다...

import sys
end = 0
while not end:
    list_command = []
    while True:
        command = sys.stdin.readline().split()
        if command[0]=="END":
            break
        elif command[0] == 'QUIT':
            end = 1
            N=0
            break
        list_command.append(command)
    if not end:
        N = int(sys.stdin.readline())
    
    for _ in range(N):
        list_stack = [int(sys.stdin.readline())]
        count = 1
        error = 0
        for command in list_command:
            if command[0] == 'NUM':
                list_stack.append(int(command[1]))
                count+=1
            elif count >0 and command[0] == 'POP':
                list_stack.pop()
                count-=1
            elif count >0 and command[0] == 'INV':
                list_stack[-1] *= -1
            elif count >0 and command[0] == 'DUP':
                list_stack.append(list_stack[-1])
                count+=1
            elif count >1 and command[0] == 'SWP':
                save1 = list_stack.pop()
                save2 = list_stack.pop()
                list_stack.append(save1)
                list_stack.append(save2)
            elif count >1 and command[0] == 'ADD':
                save1 = list_stack.pop()
                save2 = list_stack.pop()
                count-=1
                list_stack.append(save1 + save2)
            elif count >1 and command[0] == 'SUB':
                save1 = list_stack.pop()
                save2 = list_stack.pop()
                count-=1
                list_stack.append(save2 - save1)
            elif count >1 and command[0] == 'MUL':
                save1 = list_stack.pop()
                save2 = list_stack.pop()
                count-=1
                list_stack.append(save1 * save2)

            
            elif count > 1 and command[0] == "DIV":
                save1 = list_stack.pop()
                save2 = list_stack.pop()
                count-=1
                if not save1:
                    error = 1
                    break
                if save1*save2>0:
                    list_stack.append(save2//save1)
                else:
                    list_stack.append(abs(save2)//abs(save1) * -1)
            elif count > 1 and command[0] == "MOD":
                save1 = list_stack.pop()
                save2 = list_stack.pop()
                count-=1
                if not save1:
                    error = 1
                    break
                if save2 < 0:
                    list_stack.append(abs(save2)%abs(save1) * -1)
                else:
                    list_stack.append(abs(save2)%abs(save1))
                

            else:
                error = 1
                break
            if count > 0 and abs(list_stack[-1]) > 10**9:
                error = 1
                break
        if count == 1 and not error:
            print(list_stack[0])
        else:
            print('ERROR')
        
    if not end:
        sys.stdin.readline()
        print()
