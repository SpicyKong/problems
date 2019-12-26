# https://www.acmicpc.net/problem/2812 문제 제목 : 크게 만들기 , 언어 : Python, 날짜 : 2019-12-26, 결과 : 성공
# 어제풀던 로봇 조종하기[2169] 풀다 하루가 마무리되었다. 결국 풀지못햇지만..
# 잘하고 싶다.

import sys
N, K = map(int, sys.stdin.readline().split())
input_num = sys.stdin.readline()[:-1]
list_stack = [input_num[0]]
count = 0
for i in range(1,N):
    while K>0 and list_stack[-1] < input_num[i]:
        list_stack.pop()
        K-=1
        if not len(list_stack):
            break
    list_stack.append(input_num[i])
print("".join(list_stack[:N-K]))
