# https://www.acmicpc.net/problem/1799 문제 제목 : 비숍 , 언어 : Python, 날짜 : 2020-03-26, 결과 : 성공
"""
    회고:
    내일 N-queen문제와 이 비숍문제를 한번 더 풀어봐야겠다. 두 문제다 내 머릿속에서 나온것이 하나도 없다..
    모두 검색을 통해서 구현했다.. 물론 그만큼 풀이의 흐름을 이해하려고 더욱 노력했다. 그러니깐 내일 한번 더 풀어보자.
    내가 만들어낸 지식이 아닌 다른분들의 지식이지만 그마저도 학습한다는 생각으로.
    노력하자.
"""
import sys
def dfs(now_x, now_y, count):
    global result, color
    
    if now_x >= N:
        now_y+=1
        if now_x%2 == 0:
            now_x = 1
        else:
            now_x = 0
        now_x = now_x%N
    if now_y >= N:
        if count > result[color]:
            result[color] = count
            #print(color, '   ', list_slash,list_slash_r)
        return
    if list_map[now_y][now_x] and list_slash[now_x+now_y] == list_slash_r[N-1-now_x+now_y] == 0:
        list_slash[now_x+now_y] = list_slash_r[N-1-now_x+now_y] = 1
        dfs(now_x+2, now_y, count+1)
        list_slash[now_x+now_y] = list_slash_r[N-1-now_x+now_y] = 0
    dfs(now_x+2, now_y, count)
    

    

N = int(sys.stdin.readline())
list_map =[list(map(int, sys.stdin.readline().split())) for _ in range(N)]

list_slash = [0]*(2*N-1)
list_slash_r = [0]*(2*N-1)
result = [0,0]
color = 0
dfs(0,0,0)
color = 1
dfs(1,0,0)
print(result)
