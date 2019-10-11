# https://www.acmicpc.net/problem/9461 문제 제목 : 파도반 수열 , 언어 : Python, 날짜 : 2019-10-11, 결과 : 성공

import sys

list_a = [1,1,1]
now_len = 3
N = int(sys.stdin.readline())
for i in range(N):
    num = int(sys.stdin.readline())
    if num > now_len:
        for _ in range(num - now_len):
            list_a.append(list_a[-1-1]+list_a[-1-2])
    print(list_a[num-1])
