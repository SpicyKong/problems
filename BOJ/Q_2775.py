# https://www.acmicpc.net/problem/2775 문제 제목 : 부녀회장이 될테야 , 언어 : Python, 날짜 : 2019-12-31, 결과 : 성공
# 오늘 졸업식했다 :P

import sys
T = int(sys.stdin.readline())

list_apt = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14]] + [[0]*14 for _ in range(14)]
for i in range(1,15):
    for j in range(14):
        list_apt[i][j] = sum(list_apt[i-1][:j+1])
for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    print(list_apt[k][n-1])
