# https://www.acmicpc.net/problem/2075 문제 제목 : N번째 큰 수 , 언어 : Python, 날짜 : 2020-04-10, 결과 : 성공
"""
    회고:
    메모리 제한이 12mb다. 따라서 불필요한 입력은 저장하지 않고 해야한다.
    그래서 나는 1줄 입력받고 처리하고 입력받고 처리하고를 반복했다.
    이 방법의 장점은 이렇게 힙의 사이즈를 정하고 처리해주면 자동으로 가장 첫번째 원소에 우리가 원하는 수가 오게된다.
"""

import sys
import heapq
N = int(sys.stdin.readline())
check = 0
list_queue = []
for _ in range(N):
    list_input = list(map(int, sys.stdin.readline().split()))
    for i in range(N):
        heapq.heappush(list_queue, list_input[i])
        if check:
            heapq.heappop(list_queue)
    check = 1
print(list_queue[0])
