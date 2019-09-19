# 아직 푸는중인데 할게 많아서 미완성으로 올립니다..ㅠ
# 2차원 리스트를 복사하니 자꾸만 얕은복사가되서 삽질했습니다..
# https://www.acmicpc.net/problem/2573 문제 제목 : 빙산 , 언어 : Python, 날짜 : 2019-09-18, 결과 : 실패
# https://www.acmicpc.net/problem/2573 문제 제목 : 빙산 , 언어 : Python, 날짜 : 2019-09-19, 결과 : 실패
# 내일 다시 시도..
# ver 2. 요즘 뭔가 할게 많아서 문제가 손에 안잡힌다..
import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())

list_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

count_year = 1
list_queue = deque()


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


list_visit = [[0]*M for _ in range(N)]
finish = False
count_year = 0
while not finish:
    count_bingsan = 0
    for y in range(N):
        for x in range(M):
            if list_map[y][x] and list_visit[y][x] == 0:
                list_queue.append([x, y])
                while list_queue:
                    tx, ty = list_queue.popleft()
                    list_visit[ty][tx] += 5
                    for i in range(4):
                        ax = tx + dx[i]
                        ay = ty + dy[i]
                        if 0 <= ax < M and 0 <= ay < N:
                            if list_map[ay][ax] and list_visit[ay][ax]==0:
                                list_visit[ay][ax]=1
                                list_queue.append([ax, ay])
                            if list_map[ay][ax]:
                                list_visit[ty][tx] -= 1
                count_bingsan+=1
    first = 0
    for y in range(N):
        for x in range(M):
            if list_visit[y][x] > 0:
                if not first:
                    first = 1
                    list_map[y][x]-=1
                if list_map[y][x] - list_visit[y][x] + 2 < 0:
                    list_map[y][x] = 0
                else:
                    list_map[y][x] -= list_visit[y][x] - 2
                list_visit[y][x] = 0
    count_year+=1
    if count_bingsan > 1:
        print(count_year)
        finish = True
    
    #[print(a) for a in list_map]
    #print("++++++++++++++++++++++++++++++")
    #[print(a) for a in list_visit]
    #print("========================================")
    
    
    
    
"""  ver 1.
import sys

#a = list(map(int,sys.stdin.readline().split()))
#b = a[:]
#b[1] = 'asdf'
#print(a)
N,M = map(int,sys.stdin.readline().split())
list_map = [list(map(int,sys.stdin.readline().split())) for _ in range(int(N))]

list_map_copy =  [a[:] for a in list_map]
#list_map = [a[:] for a in list_map]
num = 0

while(True):
    count_a = 0
    for n in range(N):
        for m in range(M):
            count=0
            c_b = 0
            if list_map[n][m] > 0:
                try:
                    if list_map[n-1][m] == 0:
                        count+=1
                except:
                    pass
                try:
                    if list_map[n+1][m] == 0:
                        count+=1
                except:
                    pass
                try:
                    if list_map[n][m-1] == 0:
                        count+=1
                except:
                    pass
                try:
                    if list_map[n][m+1] == 0:
                        count+=1
                except:
                    pass
                if count>0:
                    #print(list_map[n][m], list_map_copy[n][m])
                    list_map_copy[n][m]=list_map_copy[n][m] - count
                    #print(list_map[n][m], list_map_copy[n][m])
                    if list_map_copy[n][m]<0:
                        list_map_copy[n][m]=0
                    count_a+=1
    num+=1

    if count_a == 0:
        [print(fdsa) for fdsa in list_map]
        print(" ")
        [print(asdf) for asdf in list_map_copy]
        print("------------------------------------")
        break
    list_map= [b[:] for b in list_map_copy]
    
print(num-1)

"""
