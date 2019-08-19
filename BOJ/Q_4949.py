# https://www.acmicpc.net/problem/4949 문제 제목 : 균형잡힌 세상 , 언어 : Python, 날짜 : 2019-08-19, 결과 : 성공

while True:
    test_str = input()
    if test_str=='.':
        break
    stack_str = []
    count = 0
    for a in test_str:
        
        if a=='[' or a =='(':
            stack_str.append(a)
        elif a==']' or a==')':
            if len(stack_str) > 0 and stack_str[-1]== '[' and a == ']':
                stack_str.pop()
            elif len(stack_str) > 0 and stack_str[-1]== '(' and a == ')':
                stack_str.pop()
            elif len(stack_str) > 0 and not stack_str[-1]== '[' and a == ']':
                count+=1
                break
            elif len(stack_str) > 0 and not stack_str[-1]== '(' and a == ')':
                count+=1
                break
            elif len(stack_str) == 0:# or not stack_str[-1]== a:
                count+=1
                break
    if len(stack_str) > 0:
        count+=1
    if count>0:
        print('no')
    else:
        print('yes')
