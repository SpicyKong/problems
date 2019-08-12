# https://www.acmicpc.net/problem/7576 문제 제목 : 토마토 , 언어 : Python, 날짜 : 2019-08-12, 결과 : 실패(시간초과)

import sys

x,y =map(int, sys.stdin.readline().split())

list_tomato = [sys.stdin.readline().split() for _ in range(y)]
tomato = True
thereistomato = 0
count=0
while(tomato):
    thereistomato = 0
    for a,b in enumerate(list_tomato):
        for c,d in enumerate(b):
            #print("asdf")
            #print(d)
            if d=='1':
                if not a==0 and not list_tomato[a-1][c] =='-1' and not list_tomato[a-1][c] =='1':
                    list_tomato[a-1][c]='2'
                    if thereistomato==0:
                        thereistomato+=1
                if not a == y-1 and not list_tomato[a+1][c] =='-1' and not list_tomato[a+1][c] =='1':
                    list_tomato[a+1][c]='2'
                    if thereistomato==0:
                        thereistomato+=1
                if not c==0 and not list_tomato[a][c-1] =='-1' and not list_tomato[a][c-1] =='1':
                    list_tomato[a][c-1]='2'
                    if thereistomato==0:
                        thereistomato+=1
                if not c == x-1 and not list_tomato[a][c+1] =='-1' and not list_tomato[a][c+1] =='1':
                    list_tomato[a][c+1]='2'
                    if thereistomato==0:
                        thereistomato+=1
    for a,b in enumerate(list_tomato):
        for c,d in enumerate(b):
            if d=='2':
                list_tomato[a][c]='1'
    if thereistomato==0:
        break
    count+=1
asdf = 0
for a,b in enumerate(list_tomato):
    for c,d in enumerate(b):
        if d=='0':
            print('-1')
            asdf =1
if asdf==0:
    print(count)
