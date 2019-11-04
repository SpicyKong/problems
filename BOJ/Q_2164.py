# https://www.acmicpc.net/problem/2164 문제 제목 : 카드2 , 언어 : Python, 날짜 : 2019-11-04, 결과 : 성공

import sys
from collections import deque
N = int(sys.stdin.readline())
list_a = deque(range(1,N+1))
while True:
    try:
        a = list_a[1]
        list_a.popleft()
        list_a.append(list_a.popleft())
    except:
        break
print(list_a[0])
