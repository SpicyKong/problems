# https://www.acmicpc.net/problem/1461 문제 제목 : 도서관 , 언어 : Python, 날짜 : 2020-03-14, 결과 : 실패
"""
    일기:
    오늘 소마 코테가 있었다. 자세한 문제내용을 언급할수는 없지만 많이 아쉽다.
    내가 평소 익숙하지 않았던 분야의 문제들도 나와서 속성으로 급하게 공부하느냐
    준비가 부족했던것 같다. 알고리즘 문제들도 있었는데 한가지를 못풀어서 많이 아쉽다.
    내년에는 제대로 준비해서 도전해야겠다.
"""
import sys
N, M = map(int, sys.stdin.readline().split())
list_inputs = list(map(int, sys.stdin.readline().split()))
list_minus = []
len_minus = 0
list_plus = []
len_plus = 0
while list_inputs:
    num = list_inputs.pop()
    if num >0:
        list_plus.append(num)
        len_plus+=1
    else:
        list_minus.append(num)
        len_minus+=1
list_minus.sort()
list_plus.sort()
m_point = len_minus%M
p_point = len_plus%M
count = M
result = 0
while list_minus:
    num = list_minus.pop()
    if count == M:
        result += abs(num)*2
    count -= 1
    if count == 0:
        count = M
count = p_point-1
while list_plus:
    num = list_plus.pop()
    if count == M:
        result += num*2
    count -= 1
    if count == 0:
        count = M
print(result-num)
'''
11 + 11
28 + 28
37 + 37
39
'''
