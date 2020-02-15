# https://www.acmicpc.net/problem/3101 문제 제목 : 토끼의 이동 , 언어 : Python, 날짜 : 2019-11-25, 결과 : 실패
# https://www.acmicpc.net/problem/3101 문제 제목 : 토끼의 이동 , 언어 : Python, 날짜 : 2020-02-15, 결과 : 성공

""" 
    회고 :

    알고리즘방에서 힌트를 자문했더니 어떠분께서 당연하지만 굉장한 핵심아이디어를 제공해 주셨다..
    바로 현재 좌표를 (i,j)라 할때 i+j를 통해 몇번째 대각선인지 구할수있다.
    이것만 알아내면 짝수,홀수를 구별하거나 크기를 비교하는등 거의 하드코딩정도로 코드를 짜면 답을 도출해낼수있다.

"""

import sys

N, K = map(int, sys.stdin.readline().split())
list_command = list(sys.stdin.readline().strip())
# 0,0에서 시작
def now(i,j):
    global N
    line = i + j
    if line < N:
        if not line%2: # />
            save = (line+1)*(line+2)//2
            save -= j
        else: # </
            save = line*(line+1)//2 + 1
            save += j
    else:
        i_save = (N-1-j)
        j_save = (N-1-i)
        i = i_save
        j = j_save
        line = 2*(N-1) - line
        if line%2: # />
            save = (line+1)*(line+2)//2
            save -= j
        else: # </
            save = line*(line+1)//2 + 1
            save += j
        save = N*N - save + 1
    return save
result = 1
x,y = 0,0
for command in list_command:

    if command=='D':
        y+=1
    elif command == 'R':
        x+=1
    elif command == 'L':
        x-=1
    else:
        y-=1
    a = now(x,y)
    result += a
print(result)












# 실패코드.1
import sys

N, K = map(int, sys.stdin.readline().split())
list_jump = list(sys.stdin.readline())

list_a = [[0]*N for _ in range(N)]
x, y = 0, 0
mode = 0 # 0=아래로 1=위로
for i in range(1, N**2+1):
    list_a[y][x] = i
    if not mode:
        if y == 0:
            x+=1
            mode = 1
        elif x == N-1:
            y+=1
            mode = 1
        else:
            y-=1
            x+=1
    else:
        if y == N-1:
            x+=1
            mode = 0
        elif x == 0:
            y+=1
            mode = 0
        else:
            x-=1
            y+=1
now_x, now_y = 0,0
result = 0
for direction in list_jump:
    result += list_a[now_y][now_x]
    if direction == 'D':
        now_y += 1
    elif direction == 'U':
        now_y -= 1
    elif direction == 'R':
        now_x += 1
    elif direction == 'L':
        now_x -= 1
print(result)
