# https://www.acmicpc.net/problem/5567 문제 제목 : 결혼식 , 언어 : Python, 날짜 : 2019-12-13, 결과 : 성공

import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

list_friend = [[] for _ in range(n+1)]
list_friends = [0 for _ in range(n+1)]
list_friends[1] = 1
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    list_friend[a].append(b)
    list_friend[b].append(a)
count = 0

for i in list_friend[1]:
    if not list_friends[i]:
        list_friends[i] = 1
        count+=1
    for j in list_friend[i]:
        if not list_friends[j]:
            list_friends[j] = 1
            count += 1
print(count)
