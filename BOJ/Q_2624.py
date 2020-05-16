# https://www.acmicpc.net/problem/2624 문제 제목 : 동전 바꿔주기 , 언어 : Python, 날짜 : 2020-05-16, 결과 : 실패
"""
    회고:
    dp문제인데, 먼가 bfs로 될거 같아서 시도해 보았다. 근데 풀다 문제를 다시 읽어보니 최대 2^31정도의 값이 나올 수 있다고 했다..
    당연히 시간초과가 떳다. 그래도 내가 풀이한 방법은 이렇다.
    현재 가지고 있는 숫자들을 해시 테이블에 저장한다. (키는 0부터 K-1까지)
    그리고 가지고 있는 숫자들의 개수를 정수로 나타낸다. ex. 123이면 오른쪽부터 0번 인덱스로 쳐서 hash[0]은 3개, hash[1]은 2개, hash[2]은 1개
    가지고 있는 숫자가 0보다 크면 하나씩 뺴주면서 BFS를 돌린다.
    그리고 가지고 있는 숫자들의 개수를 정수로 나타낸것을 이용해 visit을 체크한다.
    시간초과다.
"""

import sys
from collections import deque


T = int(sys.stdin.readline())
K = int(sys.stdin.readline())
list_num = [0]*(T+1)
set_check = set()
dict_num = {}
i = K-1
imsi = ''
for _ in range(K):
    cost, count = sys.stdin.readline().split()
    imsi+=count
    dict_num[i] = int(cost)
    i-=1
list_queue = deque()
list_queue.append((0, int(imsi)))
t = 1
while list_queue:
    #print(t)
    t+=1
    now_num, now_coins = list_queue.popleft()
    check = 0
    while now_coins >= 10**check and K > check:
        next_coin = now_coins%10**(check+1)//(10**check)
        next_coins = now_coins-10**check
        next_num = now_num+dict_num[check]
        if next_coin and not next_coins in set_check and next_num <= T:
            if next_num == T:
                list_num[next_num]+=1
            set_check.add(next_coins)
            list_queue.append((next_num, next_coins))

        check+=1
print(list_num[-1])
