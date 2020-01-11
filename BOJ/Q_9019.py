# https://www.acmicpc.net/problem/9019 문제 제목 : DSLR , 언어 : Python, 날짜 : 2020-01-11, 결과 : 성공
# 처음 봤을때는 그냥 BFS돌리면 풀리겠구나 했는데 생각치도 못한곳에서 발목을 잡혔다.
# 맨처음에는 함수 D,S,L,R을 각각 선언했다. 함수 L,R의 리턴값을 구하는 과정에서 스트링을 쓰면 편리하다고 생각해서
# 정수형 > 문자열 > 정수형 이런식의 형변환이 이루어 지게끔 코드를 작성했다. 하지만 이 부분이 문제였다.
# 그래서 결국 질문게시판을 돌아다니며 다른분들의 L, R 부분의 코드를 참고해 코드를 완성시켰다.
# 왜 이런생각을 하지 못했을까..
# 맨 아래에는 맨 처음 작성했던 시간초과가 났던 코드를 첨부한다.

import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):

    A, B = map(int, sys.stdin.readline().split())
    list_queue = deque([A])
    list_check = [0]*10000#{i:0 for i in range(10000)}
    list_str = ['D', 'S', 'L', 'R']

    while list_queue:
        num = list_queue.popleft()
        if num == B:
            break
        for i in range(4):
            if i == 0: # D
                num_save = (num*2)%10000
            elif i == 1: # S 
                if num > 0: 
                    num_save = num - 1
                else:
                    num_save = 9999
            elif i == 2: # L
                num_save = (num % 1000) * 10 + num//1000
            else: # R
                num_save = (num // 10) + (num%10) * 1000
            if not list_check[num_save]:
                list_check[num_save] = [num, list_str[i]]
                list_queue.append(num_save)
    
    list_result = []
    last_num = B
    count = 0
    while not last_num == A:
        last_num, action = list_check[last_num]
        list_result.append(action)
        count+=1
    for i in range(count):
        print(list_result[-1 - i], end = '')
    print()
    
# 시간초과 코드(아래)
import sys
from collections import deque

def D(N):
    return (N*2)%10000
def S(N):
    if N > 0:
        return N-1
    else:
        return 9999
def L(N):
    return int(N[1] + N[2] + N[3] +N[0])
    #list_N = deque(str(N))
    #list_N.append(list_N.popleft())
    #return int("".join(list_N))
    #return 
def R(N):
    #list_N = deque(str(N))
    #list_N.appendleft(list_N.pop())
    #return int("".join(list_N))
    return int(N[3] + N[0] + N[1] +N[2])
#print(L(4123))

T = int(sys.stdin.readline())
for _ in range(T):

    A, B = map(int, sys.stdin.readline().split())
    list_queue = deque([A])
    list_check = [0]*10000#{i:0 for i in range(10000)}
    list_func = [D, S, L, R]
    list_str = ['D', 'S', 'L', 'R']

    while list_queue:
        num = list_queue.popleft()
        num_str = str(num)
        num_str = '0'*(4 - len(num_str)) + num_str
        if num == B:
            break
        for i in range(4):
            if i <= 1:
                num_save = list_func[i](num)
            else:
                num_save = list_func[i](num_str)
            if not list_check[num_save]:
                list_check[num_save] = [num, list_str[i]]
                list_queue.append(num_save)
    
    list_result = []
    last_num = B
    count = 0
    while not last_num == A:
        last_num, action = list_check[last_num]
        list_result.append(action)
        count+=1
    for i in range(count):
        print(list_result[-1 - i], end = '')
    print()
