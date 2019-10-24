# https://www.acmicpc.net/problem/9095 문제 제목 : 1, 2, 3 더하기 , 언어 : Python, 날짜 : 2019-10-24, 결과 : 성공
# 이 문제는 걍 미리 dp 리스트를 구해서 빠르게(?)출력했다.

import sys
for _ in range(int(sys.stdin.readline())):
    print([1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274][int(sys.stdin.readline())])#, 504, 927, 1705][int(sys.stdin.readline())])#, 232, 376]
"""
for i in range(11):
    dp_list.append(dp_list[-1] + dp_list[-2] + dp_list[-3] )
print(dp_list)
"""
#for _ in range(int(sys.stdin.readline())):
#    N = int(sys.stdin.readline())

"""
0 1 2 3 4 5 6 7 8 9 10
0 1 2 4 7
"""
