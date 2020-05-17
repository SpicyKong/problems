# https://www.acmicpc.net/problem/1669 문제 제목 : 멍멍이 쓰다듬기 , 언어 : Python, 날짜 : 2020-05-17, 결과 : 성공
"""
    회고:
    1로 시작해 1로 끝나야 한다. 그리고 이 조건으로 인해 좀만 더 생각해 보면 아래와 같이 생각을 할 수 있다.
    1*1=1  | 1
    2*2=4  | 1 2 1
    3*3=9  | 1 2 3 2 1
    4*4=16 | 1 2 3 4 3 2 1
    위의 표를 보면 알 수 있듯이 키의 차이가 어느 수들 사이에 있는지만 알면 쉽게 결과값을 구할 수 있다.

    오늘부터 제대로 웹을 시작할건데 열심히 해봐야겠다.
"""
import sys
x, y = map(int, sys.stdin.readline().split())
gap = y - x
root = int(gap**0.5)
result=root*2-1
if result < 0:
    result = 0
if gap - root**2 == 0:
    pass
elif gap - root**2 <= root:
    result+=1
else:
    result+=2
print(result)

"""
1*1=1  | 1
2*2=4  | 1 2 1
3*3=9  | 1 2 3 2 1
4*4=16 | 1 2 3 4 3 2 1

"""
