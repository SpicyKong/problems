# https://www.acmicpc.net/problem/17822 문제 제목 : 원판 돌리기 , 언어 : Python, 날짜 : 2020-02-24, 결과 : 성공
"""
    회고:
    이 문제는 티어에 비해 쉬워보여서 잡았는데 구현을 하면 할 수록 뭔가 복잡했다.
    그나마 다행인 점은 복잡해도 그냥 꾸역꾸역 구현해 나가면 풀린다.
"""
import sys
from collections import deque

def spin_dish(x, d, k):
    global list_dishes, N, list_check
    count = 1
    while count * x <= N:
        for _ in range(k):
            if d:
                list_dishes[count * x-1].append(list_dishes[count * x-1].popleft())
                list_check[count * x-1].append(list_check[count * x-1].popleft())
            else:
                list_dishes[count * x-1].appendleft(list_dishes[count * x-1].pop())
                list_check[count * x-1].appendleft(list_check[count * x-1].pop())
        count +=1

N, M, T = map(int, sys.stdin.readline().split())
list_dishes = [deque(map(int, sys.stdin.readline().split())) for _ in range(N)]
list_command = [list(map(int, sys.stdin.readline().split())) for _ in range(T)]
list_check = [deque([0]*M) for _ in range(N)]
count = 1
list_delete = []
now_sum = 0
now_count = 0
for i in range(N):
    for j in range(M):
        now_sum+= list_dishes[i][j]
        now_count+=1
for command in list_command:
    spin_dish(*command)
    for i in range(N):
        for j in range(M-1,-1,-1):
            if list_dishes[i][j] > 0 and list_dishes[i][j] == list_dishes[i][j-1]:
                if (not list_check[i][j] or list_check[i][j] == count) and (not list_check[i][j-1] or list_check[i][j-1] == count):
                    if not list_check[i][j]:
                       list_check[i][j] = count
                       list_delete.append([i,j])
                    if not list_check[i][j-1]:
                        list_check[i][j-1] = count
                        list_delete.append([i,j-1])
            if N-1 > i and list_dishes[i][j] > 0 and list_dishes[i][j] == list_dishes[i+1][j]:
                if (not list_check[i][j] or list_check[i][j] == count) and (not list_check[i+1][j] or list_check[i+1][j] == count):
                    if not list_check[i][j]:
                        list_check[i][j] = count
                        list_delete.append([i,j])
                    if not list_check[i+1][j]:
                        list_check[i+1][j] = count
                        list_delete.append([i+1,j])
    count +=1
    if list_delete:
        while list_delete:
            y, x = list_delete.pop()
            now_sum -= list_dishes[y][x]
            now_count-=1
            list_dishes[y][x] = 0
    else:
        save_sum = now_sum
        for i in range(N):
            for j in range(M):
                if list_dishes[i][j] > now_sum/now_count:
                    list_dishes[i][j] -= 1
                    save_sum -= 1
                elif 0 < list_dishes[i][j] < now_sum/now_count:
                    list_dishes[i][j] += 1
                    save_sum += 1
        now_sum = save_sum
    if not now_count:
        now_sum = 0
        break
print(now_sum)
