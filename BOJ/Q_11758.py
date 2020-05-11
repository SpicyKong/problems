# https://www.acmicpc.net/problem/11758 문제 제목 : CCW , 언어 : Python, 날짜 : 2020-05-11, 결과 : 성공
"""
    회고:
    사실 다른 문제를 풀다가 CCW알고리즘에 대해 알게 되었다. 방향 벡터를 이용해 3점의 상태를 파악하는 알고리즘인데,
    솔직하게 자세히 증명을 하지는 못했다. 그러니깐 아이패드로 증명 과정을 봐야겠다. 
"""
import sys

x1, y1 = map(int, sys.stdin.readline().split())
x2, y2 = map(int, sys.stdin.readline().split())
x3, y3 = map(int, sys.stdin.readline().split())

ccw = (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)
print(ccw)
if ccw > 0:
    print(1)
elif ccw < 0:
    print(-1)
else:
    print(0)
