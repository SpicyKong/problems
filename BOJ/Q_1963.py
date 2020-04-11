# https://www.acmicpc.net/problem/1963 문제 제목 : 소수 경로 , 언어 : Python, 날짜 : 2020-04-11, 결과 : 성공
"""
    회고:
    처음에는 그냥 str()과 int()를 적절히 사용해가며 풀려고 했는데 저번에 str()을 남발했다가 문제를 틀린적이있어서
    입력받을때만 형변환하고 그 이후로 안하고 풀었다. 문제는 간단하다. 맨처음에 에라토스테네스의 체로 소수들을 찾아주고
    BFS를 돌려주면 된다. 정수의 i번쨰(뒤에서부터) 수를 구하는 방법으로는 난 그냥 %(10**(i+1))//10**i 이런식으로 구해주었다.
    최근에 BFS문제를 건드린적이 없는거 같은데 뭔가 BFS문제를 푸니 행복하다ㅋㅋ

    이제 잠깐 쉬다가 최근에 봤던 코포 업솔빙 하러가야겠다.
    확실히 코드포스는 지문이 와닿지 않아서 그런지 너무 어렵다..

"""

import sys
from collections import deque

T = int(sys.stdin.readline())
list_sosu = [1]*10000
list_sosu[0] = 0
list_sosu[1] = 0
for i in range(2,int(10000**0.5)+1):
    
    if list_sosu[i]:
        count = 2
        while count * i < 10000:
            list_sosu[i*count] = 0
            count+=1

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    end = -1
    list_visit = [0]*10001
    list_queue = deque()
    list_queue.append([A, 0])
    while list_queue:
        now_num, now_count = list_queue.popleft()
        if now_num == B:
            end = now_count
            break
        for i in range(4):
            i+=1
            save_num = now_num + 10**(i-1)
            while save_num < 10000 and now_num%(10**(i+1))//10**i == save_num%(10**(i+1))//10**i:
                if not list_visit[save_num] and list_sosu[save_num]:
                    list_queue.append([save_num, now_count+1])
                save_num += 10**(i-1)

            save_num = now_num - 10**(i-1)
            while save_num > 1000 and now_num%(10**(i+1))//10**i == save_num%(10**(i+1))//10**i:
                if not list_visit[save_num] and list_sosu[save_num]:
                    list_visit[save_num] = 1
                    list_queue.append([save_num, now_count+1])
                save_num -= 10**(i-1)
    if end>=0:
        print(end)
    else:
        print('Impossible')
