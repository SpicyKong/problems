# https://www.acmicpc.net/problem/1297 문제 제목 : TV 크기 , 언어 : Python, 날짜 : 2019-10-19, 결과 : 성공

import sys
a, b, c = map(int, sys.stdin.readline().split())
#대각선 높이 너비
# 대각**2 = (높이비 * a) ** 2 + (너비비 * a) ** 2
#         = 높**2 * a**2 + 너**2 * a**2
#         = a**2 * (높**2 + 너**2)
# 대각 ** 2 / (높**2 + 너**2) = a**2
d = (a**2/(b**2 + c**2))**0.5
print(int(b*d), int(c*d))
