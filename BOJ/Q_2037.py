# https://www.acmicpc.net/problem/2037 문제 제목 : 문자메시지 , 언어 : Python, 날짜 : 2019-12-08, 결과 : 성공
# 이 문제는 맨첨에 입력받을때 sys.stdin.readline()[:-1] 이런식으로 입력을 받았는데
# 맞는데 자꾸 틀려서 게시판을 보니 테스트케이스에 개행문자가 없는 케이스가 있다고 해서
# input()으로 바꾸어 주었더니 되었다.

import sys

p, w = map(int, sys.stdin.readline().split())
input_str = input()
list_buttons = {' ':1, 'A':2 , 'B':2, 'C':2 ,'D':3 ,'E':3 ,'F':3, 'G':4, 'H':4, 'I':4, 'J':5, 'K':5, 'L':5, 'M':6, 'N':6, 'O':6, 'P':7, 'Q':7 ,'R':7,'S':7, 'T':8, 'U':8, 'V':8, 'W':9,'X':9,'Y':9,'Z':9}
cost_buttons = {' ':p, 'A':p , 'B':p*2, 'C':p*3 ,'D':p ,'E':p*2 ,'F':p*3, 'G':p, 'H':p*2, 'I':p*3, 'J':p, 'K':p*2, 'L':p*3, 'M':p, 'N':p*2, 'O':p*3, 'P':p, 'Q':p*2 ,'R':p*3,'S':p*4, 'T':p, 'U':p*2, 'V':p*3, 'W':p,'X':p*2,'Y':p*3,'Z':p*4}
result = 0
last_key = -1
for alphabet in input_str:
    if last_key == list_buttons[alphabet] and not last_key==1:
        result+=w
    last_key = list_buttons[alphabet]
    result+=cost_buttons[alphabet]

print(result)
