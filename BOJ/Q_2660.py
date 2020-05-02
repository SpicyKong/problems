# https://www.acmicpc.net/problem/2660 문제 제목 : 회장뽑기 , 언어 : Python, 날짜 : 2020-05-02, 결과 : 성공
"""
    회고:
    내가하는 최적화는 항상 오답을 만든다..ㅠㅠ
    플로이드 와샬을 통해 모든 구하라는건 다 구해놓고 정작 최대값들의 최소값을 뽑는 과정을 자꾸 틀렸다.
    나중에 반복문 안쓰려고 그냥 연산을 할 떄마다 업데이트 시켰는데 자꾸 틀렸습니다가 뜬다.. 그래서 그냥 반복문을 써서 비 효율적으로 구했더니
    맞았다.

    오늘 레몬묘목과 핑거라임 묘목이 도착했다. 아직 화분과 상토 그리고 펄라이트? 라는게 없어서 포트에 담겨져 있는 채로 방치해 두었다. 내일은 심어야 겠다.

"""

import sys
N = int(sys.stdin.readline())
list_map = [[0 if i==j else 50*7 for i in range(N)] for j in range(N)]
while True:
    a, b = map(int, sys.stdin.readline().split())
    if a==-1 and b==-1:
        break
    list_map[a-1][b-1] = 1
    list_map[b-1][a-1] = 1
for mid in range(N):
    for start in range(N):
        for end in range(N):
            #if mid == start or mid == end:# or start == end:
            #    continue
            if list_map[start][end] > list_map[start][mid] + list_map[mid][end]:
                list_map[start][end] = list_map[start][mid] + list_map[mid][end]
list_candidate = [max(list_map[i]) for i in range(N)]
key = min(list_candidate)
count = 0
list_res = []
for i in range(N):
    if list_candidate[i] == key:
        count+=1
        list_res.append(i+1)
print(key, count)
print(*list_res)

"""
import sys
N = int(sys.stdin.readline())
list_map = [[0 if i==j else 50*7 for i in range(N)] for j in range(N)]
list_candidate = [[0,i] for i in range(N)]
while True:
    a, b = map(int, sys.stdin.readline().split())
    if a==-1 and b==-1:
        break
    list_map[a-1][b-1] = 1
    list_map[b-1][a-1] = 1
    list_candidate[a-1][0] = 1
    list_candidate[b-1][0] = 1
for mid in range(N):
    for start in range(N):
        for end in range(N):
            #if mid == start or mid == end:# or start == end:
            #    continue
            if list_map[start][end] > list_map[start][mid] + list_map[mid][end]:
                list_map[start][end] = list_map[start][mid] + list_map[mid][end]
                list_candidate[start][0] = max(list_candidate[start][0], list_map[start][end])
list_candidate.sort()
key = list_candidate[0][0]
num_candidate = 0
list_res= []
for candidate in list_candidate:
    if not candidate[0] == key:
        break
    num_candidate+=1
    list_res.append(candidate[1]+1)
print(key, num_candidate)
print(*list_res)"""
"""
8
1 8
2 7
3 4
4 6
-1 -1
"""
