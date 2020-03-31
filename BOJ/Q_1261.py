# https://www.acmicpc.net/problem/1261 문제 제목 : 알고스팟 , 언어 : Python, 날짜 : 2020-03-31, 결과 : 실패
"""
    회고:
    이 문제에 맞게 우선순위 큐를 직접 구현해 보았다. 힙 자료구조를 배웠는데 예전에도 찾아본적은 있었지만
    직접 코드로 구현해본건 처음인것 같다. 하지만 이미 구현되어 있는 모듈이 있다면 그걸 쓰는게 좋아보인다.
    이 코드는 python3에서는 시간초과 pypy3에서는 메모리 초과를 받았으니..ㅠㅠ
    그래도 다익스트라와 우선순위큐, 입 자료구조를 살펴볼수있어서 좋았다. 한번 좀더 깔끔한 코드를 짜서 다시 풀어봐야겠다.
"""


import sys
from collections import deque

def get_parent(index):
    return (index - 1)//2

def get_child_l(index):
    return index*2 + 1

def get_child_r(index):
    return index*2 + 2

def node_swap(index_a, index_b):
    global list_a
    imsi = list_a[index_a]
    list_a[index_a] = list_a[index_b]
    list_a[index_b] = imsi

def node_insert(node):
    global list_a, count
    now_count = count
    list_a.append(node)
    if now_count == 0:
        count+=1
        return
    while list_a[get_parent(now_count)][0] > list_a[now_count][0]:
        imsi = list_a[get_parent(now_count)]
        list_a[get_parent(now_count)] = list_a[now_count]
        list_a[now_count] = imsi
    count+=1

def node_pop():
    global count, list_a
    if count == 1:
        count-=1
        return list_a.pop()
    result = list_a[0]
    list_a[0] = list_a.pop()
    count -= 1
    now_count = 0
    end = 0
    while not end:
        child_r = get_child_r(now_count)
        child_l = get_child_l(now_count)
        if (count > child_l and list_a[child_l][0] < list_a[now_count][0]) or (count > child_r and list_a[child_r][0] < list_a[now_count][0]):
            if count <= child_l:
                next_count = child_r
            elif count <= child_r:
                next_count = child_l
            elif list_a[child_l][0] > list_a[child_r][0]:
                next_count = child_r
            else:
                next_count = child_l
            node_swap(now_count, next_count)
            now_count = next_count
        else:
            end = 1
    return result

list_a = []
count = 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]

M,N = map(int, sys.stdin.readline().split())
list_map = [list(sys.stdin.readline().strip()) for _ in range(N)]
list_visit = [[0]*M for _ in range(N)]
list_visit[0][0] = 1
node_insert([1, 0, 0])


while list_a:
    #[print(a) for a in list_visit]
    #print('==================')
    print(list_a)
    now_count, now_x, now_y = node_pop()
    for i in range(4):
        nx = now_x + dx[i]
        ny = now_y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if (list_visit[ny][nx] >= now_count+1 or not list_visit[ny][nx]):
                if list_map[ny][nx] == '1':
                    list_visit[ny][nx] = now_count+1
                    node_insert([now_count+1, nx, ny])
                elif list_map[ny][nx] == '0':
                    list_visit[ny][nx] = now_count
                    node_insert([now_count, nx, ny])

print(list_visit[N-1][M-1]-1)

"""
node_insert(len(list_a), [13,1,3])
node_insert(len(list_a), [88,1,3])
node_insert(len(list_a), [112,1,3])
node_insert(len(list_a), [35,1,3])
node_insert(len(list_a), [17,1,3])
node_insert(len(list_a), [76,1,3])
print(list_a)
print(node_pop(len(list_a)))
print(list_a)
print(node_pop(len(list_a)))
print(list_a)
print(node_pop(len(list_a)))
print(list_a)
      0
  1       2
3   4   5   6

6 6
001111
010000
001111
110011
011110
100010

9 5
010000000
010101010
010101010
010101010
000101010
"""
