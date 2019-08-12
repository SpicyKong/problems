# https://www.acmicpc.net/problem/7576 문제 제목 : 토마토 , 언어 : Python, 날짜 : 2019-08-12, 결과 : 실패(틀렸습니다!)
#   기존의 방법에서 불필요한 조건문을 없애서 확실히 실행시간 단축에 도움이 되긴 했는데
#   계속 하다보니 10% 지점에서 틀린다. 다시 수정해봐야 겠다.

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
            if count%2==0 and d=='1':
                try:
                    if list_tomato[a-1][c] =='0':
                        list_tomato[a-1][c]='2'
                        if thereistomato==0:
                            thereistomato+=1
                except:
                    pass
                try:
                    if list_tomato[a+1][c] =='0':
                        list_tomato[a+1][c]='2'
                        if thereistomato==0:
                            thereistomato+=1
                except:
                    pass
                try:
                    if list_tomato[a][c-1] =='0':
                        list_tomato[a][c-1]='2'
                        if thereistomato==0:
                            thereistomato+=1
                except:
                    pass
                try:
                    if list_tomato[a][c+1] =='0':
                        list_tomato[a][c+1]='2'
                        if thereistomato==0:
                            thereistomato+=1
                except:
                    pass

            elif count%2==1 and d=='2':
                try:
                    if list_tomato[a-1][c] =='0':
                        list_tomato[a-1][c]='1'
                        if thereistomato==0:
                            thereistomato+=1
                except:
                    pass
                try:
                    if list_tomato[a+1][c] =='0':
                        list_tomato[a+1][c]='1'
                        if thereistomato==0:
                            thereistomato+=1
                except:
                    pass
                try:
                    if list_tomato[a][c-1] =='0':
                        list_tomato[a][c-1]='1'
                        if thereistomato==0:
                            thereistomato+=1
                except:
                    pass
                try:
                    if list_tomato[a][c+1] =='0':
                        list_tomato[a][c+1]='1'
                        if thereistomato==0:
                            thereistomato+=1
                except:
                    pass
    if thereistomato==0:
        break
    count+=1
asdf = 0
#[print(a) for a in list_tomato]
for a,b in enumerate(list_tomato):
    if '0' in b:
        print('-1')
        asdf =1
        break
if asdf==0:
    print(count)
