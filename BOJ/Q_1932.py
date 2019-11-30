# https://www.acmicpc.net/problem/1932 문제 제목 : 정수 삼각형 , 언어 : Python, 날짜 : 2019-11-30, 결과 : 성공
# 문제가 dp로 분류되어 있어서 정답률과 별개로 쫄았다..
# 문제를 풀때 주어진 조건에 상관없이 흔들리지 않고 풀수있도록 노력해야겠다.

import sys
N = int(sys.stdin.readline())
list_a = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
for i in range(1,N):
    for j, num in enumerate(list_a[i]):
        imsi = []
        if 1<= j:
            imsi.append(list_a[i-1][j-1])
        if j <= i-1:
            imsi.append(list_a[i-1][j])
        list_a[i][j] = list_a[i][j] + max(imsi)
print(max(list_a[-1]))
