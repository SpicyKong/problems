# https://www.acmicpc.net/problem/2624 문제 제목 : 동전 바꿔주기 , 언어 : Python, 날짜 : 2020-06-05, 결과 : 성공

"""
    회고:
    혼자서 삽질하다, 도저히 솔루션이 떠오르지 않아서 다른 분의 코드를 보며 작성했다.
    어떻게 이런 생각을 할 수 있는건지 잘 모르겠다. 나는 그냥 바텀업 방식으로만 생각을 해 보았는데,
    도저히 메모이 제이션이 어떤식으로 이루어 지는지 이해가 안되서 포기했었다. 근데 이 코드를 보면
    사용된 동전의 가지수를 이용해 메모이 제이션이 진행된다.. 도저히 dp는 못풀겠다..
"""

import sys
def dfs(now, count):
    global T, K
    if now == 0:
        return 1
    if count>=K:
        return 0
    if not list_memo[now][count] == -1:
        return list_memo[now][count]
    
    list_memo[now][count] = 0
    for nok in range(list_coin[count][1]+1): #NOK : num of coins
        if now - list_coin[count][0]*nok>=0:
            list_memo[now][count] += dfs(now - list_coin[count][0]*nok, count+1)
    
    return list_memo[now][count]

    
T = int(sys.stdin.readline())
K = int(sys.stdin.readline())
list_coin = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]
list_memo = [[-1]*(K+1) for _ in range(T+1)]
print(dfs(T, 0))

print('------------')
[print(a) for a in list_memo]
#list_memo[0][0] = 0
#for cost in range(T+1):
#    for coin in range(K):
#        for count in range(list_coin[coint][1]):


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
